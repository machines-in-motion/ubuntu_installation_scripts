# [BASH IGNORE]

FROM ubuntu:14.04
MAINTAINER Vincent Berenz <vincentberenz@tuebingen.mpg.de>

###################################################################################
# This Dockerfile is also used to generate the official image install ssh 
# script. (see desktop_update folder in amd-clmc/official_images)
# The [BASH IGNORE*]  [/BASH IGNORE*] ; [SSH ONLY*] [/SSH ONLY*] tags are here to indicate
# what will go in the official ssh install script and what will not
###################################################################################

# [/BASH IGNORE]

###############################################################################
# We add all other repositories.
###############################################################################

RUN apt-get update && \
    apt-get -y install curl wget

RUN apt-get update && apt-get install -y software-properties-common

RUN apt-add-repository -y ppa:ubuntu-elisp/ppa
RUN apt-add-repository -y ppa:libccd-debs
RUN apt-add-repository -y ppa:fcl-debs
RUN apt-add-repository -y ppa:dartsim


RUN echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list && \
    wget http://packages.ros.org/ros.key -O - | apt-key add -

RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash


RUN apt-get update && \
    apt-get install -y \
    python-catkin-tools \
    python-rosdep \
    python-rosinstall \
    python-rospkg \
    python-wstool \
    ros-indigo-audio-common \
    ros-indigo-catkin \
    ros-indigo-cmake-modules \
    ros-indigo-control-toolbox \
    ros-indigo-desktop-full \
    ros-indigo-driver-common \
    ros-indigo-ecto \
    ros-indigo-fcl \
    ros-indigo-gazebo-ros-control \
    ros-indigo-gazebo-ros-pkgs \
    ros-indigo-joint-state-publisher \
    ros-indigo-joy \
    ros-indigo-kdl-parser \
    ros-indigo-keyboard \
    ros-indigo-octomap \
    ros-indigo-octomap-msgs \
    ros-indigo-octomap-rviz-plugins \
    ros-indigo-ompl \
    ros-indigo-openni-* \
    ros-indigo-pcl-conversions \
    ros-indigo-qt-build \
    ros-indigo-realtime-tools \
    ros-indigo-robot-state-publisher \
    ros-indigo-ros-control \
    ros-indigo-ros-controllers \
    ros-indigo-tf-conversions \
    ros-indigo-tf-conversions \
    ros-indigo-robot-self-filter \
    ros-indigo-xacro 

RUN rosdep init && rosdep update

RUN apt-get install -y \
    apt-file \
    alien \
    asciidoc \
    autoconf \
    autofs \
    awesome \
    bash-completion \
    bc \
    binutils \
    build-essential \
    build-essential \
    ccache \
    cmake \
    cmake \
    cmake-curses-gui \
    curl \
    curl \
    doxygen \
    emacs-snapshot \
    f2c \
    freeglut3 \
    freeglut3-dev \
    gdb \
    gfortran \
    git-lfs \
    git-svn \
    imagemagick \
    iputils-ping \
    less \
    libace-dev \
    libblas-dev \
    libc6-dev \
    libcairo2-dev \
    libconfig++8-dev \
    libdart5-dev \
    libdbus-1-dev \
    libedit-dev \
    libedit-dev \
    libeigen3-dev \
    libeinspline-dev \
    libeinspline-dev \
    libevent-dev \
    libf2c2-dev \
    libffi-dev \
    libgflags-dev \
    libgflags2 \
    libgirepository1.0-dev \
    libglew1.6-dev \
    libgoogle-glog-dev \
    libhdf5-dev \
    liblapack-dev \
    liblua5.1-0-dev \
    libncurses5-dev \
    libpango1.0-dev \
    libslicot-dbg \
    libslicot-dev \
    libslicot0 \
    libssl-dev \
    libstartup-notification0-dev \
    libwxgtk2.8-dbg \
    libwxgtk2.8-dev \
    libx11-xcb-dev \
    libxcb-cursor-dev \
    libxcb-icccm4-dev \
    libxcb-keysyms1-dev \
    libxcb-randr0-dev \
    libxcb-render-util0-dev \
    libxcb-shape0-dev \
    libxcb-util0-dev \
    libxcb-xinerama0-dev \
    libxcb-xkb-dev \
    libxcb-xtest0-dev \
    libxcb1-dev \
    libxdg-basedir-dev \
    libxinerama-dev \
    libxkbcommon-dev \
    libxkbcommon-x11-dev \
    libxmu-dev \
    lsb-release \
    luarocks \
    m4 \
    man \
    mesa-utils \
    net-tools \
    ntp \
    ntpdate \
    openssh-server \
    patch \
    picocom \
    python-dev \
    python-netifaces \
    python-pip \
    python-vcstool \
    python-vcstools \
    python-wstool \
    rpm \
    scons \
    screen \
    shellcheck \
    ssh \
    sshpass \
    sudo \
    swig \
    tcsh \
    vim \
    vim \
    wget \
    xmlto \
    xutils-dev \
    protobuf-compiler \
    protobuf-c-compiler 


#######
# JAVA
#######
# for some reason, that does not seem to work in docker ...
# not a big deal, for the moment necessary mostly for crashplan
######## commented: commands below broken. We should find a new way to install java
#RUN add-apt-repository ppa:webupd8team/java
#RUN apt-get -y -q update
#RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections
#RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections
#RUN apt-get -y -q install oracle-java8-installer
#RUN update-java-alternatives -s java-8-oracle

####
# apparently bazel should be installed after java
####
RUN echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list && \
    curl https://bazel.build/bazel-release.pub.gpg | sudo apt-key add -
RUN apt-get update && apt-get install -y bazel 

##################################
# cuda and gpu related libraries 
##################################

# not here because would not work from docker
# visit : scrips in <path>/amd-clmc/official_image/desktop_update/gpu
# for installation instructions


###############################################################################
# lua and awesome behaviors
###############################################################################
#RUN apt-get update && apt-get build-dep -y awesome && \
#[BASH IGNORE]
#    rm -rf /var/lib/apt/lists/*
#[/BASH IGNORE]
#RUN luarocks install lgi


###############################################################################
# required for the use of snopt 
###############################################################################
RUN wget http://ftp.gnu.org/gnu/autoconf/autoconf-2.69.tar.gz -P /tmp/ && \
    tar -xf /tmp/autoconf-2.69.tar.gz -C /tmp/ && \
    rm /tmp/autoconf-2.69.tar.gz && \
    cd /tmp/autoconf-2.69 && \
    ./configure && \
    make -C /tmp/autoconf-2.69 && \
    make install -C /tmp/autoconf-2.69

###############################################################################
# git-lfs
###############################################################################
RUN git lfs install --skip-smudge && \
    git config --global credential.helper cache && \
    git config --global credential.helper 'cache --timeout=3600'


###############################################################################
# PYTHON MODULES
###############################################################################

RUN pip install --upgrade pip
RUN pip install pyopenssl
RUN pip install --upgrade \
    colorama \
    matplotlib \
    ndg-httpsclient \
    numpy \
    pyasn1 \
    schedule \
    scipy \
    sklearn \
    virtualenv \
    appdirs \
    h5py \
    keras \
    ipython \
    ipdb \
    graphviz
RUN pip install pydot==1.0.28
RUN pip install pyparsing==2.0.1
RUN pip install --upgrade six --target="/usr/lib/python2.7/dist-packages"
RUN pip install appdirs
RUN pip install --upgrade protobuf

#[BASH IGNORE]
#########################################
# for convenience, to map workspace in it
#########################################
RUN mkdir /workspace
RUN mkdir /ssh
#[/BASH IGNORE]

########################
# start ssh agent
########################
RUN eval `ssh-agent -s`





