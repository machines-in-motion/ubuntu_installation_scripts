#!/bin/bash
# Build and install Linux kernel with preempt_rt patch on Ubuntu 22.04.

# fail on error
set -e -o pipefail

## User input, you potentially need to update or change this values during your installation

# Kernel version to install
VERSION_MAJOR=6
VERSION_SECOND=6
VERSION_MINOR=36

# directory to which kernel sources will be downloaded
DOWNLOAD_DIR="${XDG_CACHE_HOME:-$HOME/.cache}/rt_preempt_kernel_install"

# directory in which the kernel will be built
BUILD_DIR="./build"

# ==============================================================================

VERSION=$VERSION_MAJOR.$VERSION_SECOND.$VERSION_MINOR
VERSION_PATCH=$VERSION-rt35
DEFAULT_CONFIG=/boot/config-$(uname -r)

if [  ! -f  $DEFAULT_CONFIG ]; then
   echo "Configure file $FILE does not exist. Please use other file."
   exit -1
fi

if [[ -e "${BUILD_DIR}" ]]; then
   echo "Build directory ${BUILD_DIR} already exists.  Please remove it and restart."
   exit 1
fi


echo "========================================================================="
echo "==="
echo "=== Building kernel in ${BUILD_DIR}"
echo "==="
echo "========================================================================="

# Install dependencies to build kernel.
sudo apt-get install -y libelf-dev libncurses-dev libssl-dev flex bison dwarves zstd debhelper

# Install packages to test rt-preempt.
sudo apt-get install -y rt-tests

# Create folder to build kernel.
mkdir -p "${DOWNLOAD_DIR}"
mkdir -p "${BUILD_DIR}"
cd "${BUILD_DIR}"

# Download kernel version and patches.
wget --directory-prefix "${DOWNLOAD_DIR}" -nc https://mirrors.edge.kernel.org/pub/linux/kernel/v$VERSION_MAJOR.x/linux-$VERSION.tar.xz
wget --directory-prefix "${DOWNLOAD_DIR}" -nc http://cdn.kernel.org/pub/linux/kernel/projects/rt/$VERSION_MAJOR.$VERSION_SECOND/older/patch-$VERSION_PATCH.patch.xz

#xz -cd linux-$VERSION.tar.xz | tar xvf -
tar --xz -xf "${DOWNLOAD_DIR}/linux-$VERSION.tar.xz"

# Apply patch
cd linux-$VERSION/
xzcat "${DOWNLOAD_DIR}/patch-$VERSION_PATCH.patch.xz" | patch -p1

# Copy default config and prompt for configuration screen.
cp $DEFAULT_CONFIG .config

echo "Please apply the following configurations in the next step:"
echo ""
echo "General setup [Enter]"
echo "  Preemption Model (Voluntary Kernel Preemption (Desktop)) [Enter]"
echo "    Fully Preemptible Kernel (RT) [Enter] #Select"
echo ""

read -p "Please read the above instructions" yn

make menuconfig -j

scripts/config --set-str LOCALVERSION "-preempt-rt"

# Disable the SYSTEM_TRUSTED_KEYS from the config.
# SEE: https://askubuntu.com/a/1329625
scripts/config --set-str SYSTEM_TRUSTED_KEYS ""
scripts/config --set-str SYSTEM_REVOCATION_KEYS ""

# SEE: https://askubuntu.com/questions/1495051/ssl-error-building-signed-kernel
scripts/config --disable MODULE_COMPRESS_ZSTD
scripts/config --enable MODULE_COMPRESS_NONE

# Build the kernel.
echo "==="
echo "=== Start building"
echo "==="
make -j$(nproc) bindeb-pkg

echo "==="
echo "=== Install the built kernel."
echo "==="
sudo dpkg -i ../linux-headers-$VERSION_PATCH-preempt-rt_$VERSION-1_amd64.deb 
sudo dpkg -i ../linux-image-$VERSION_PATCH-preempt-rt_$VERSION-1_amd64.deb
sudo dpkg -i ../linux-libc-dev_$VERSION-1_amd64.deb

# Modify the grub setting: comment out GRUB_HIDDEN_TIMEOUT and update grub.
echo "==="
echo "=== Update grub."
echo "==="
sudo sed -i 's/GRUB_HIDDEN_TIMEOUT/# GRUB_HIDDEN_TIMEOUT/g' /etc/default/grub
sudo update-grub


echo "==="
echo "=== Reconfigure system for real-time applications."
echo "==="
# Create realtime config.
if [  ! -f  /etc/security/limits.d/99-realtime.conf ]; then
  sudo tee /etc/security/limits.d/99-realtime.conf > /dev/null <<EOL
@realtime   -   rtprio  99
@realtime   -   memlock unlimited
EOL
fi

if grep -q "realtime" /etc/group; then
  echo "Realtime group already exists"
else
  sudo groupadd realtime
fi

sudo usermod -a -G realtime $USER

# Change the permission on /dev/cpu_dma_latency. This allows other users to
# set the minimum desired latency for the CPU other than root (e.g. the current
# user from dynamic graph manager).
sudo chmod 0666 /dev/cpu_dma_latency

echo "========================================================================="
echo "==="
echo "=== Installation done. Please reboot and select new kernel from grub menu."
echo "==="
echo "=== Make sure to add all uses with rt permissions to the 'realtime' group using:"
echo "==="
echo "===  sudo usermod -a -G realtime $USER"
echo "==="
echo "========================================================================="
