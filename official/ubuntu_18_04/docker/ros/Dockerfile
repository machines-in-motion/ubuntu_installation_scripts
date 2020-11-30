# [BASH IGNORE]

FROM docker.is.localnet:5000/amd/18.04:core
MAINTAINER Vincent Berenz <vincentberenz@tuebingen.mpg.de>

# [/BASH IGNORE]

####################################################
#             ROS INSTALLATION
####################################################

# enable kernel sources
# this is necessary for the ros package librealsense in 16.04 (and 18.04 ?)
RUN apt-get install -y sudo              # Provide the sudo rights, required for the enable_kernel_sources.sh script file below
RUN wget -O enable_kernel_sources.sh http://bit.ly/en_krnl_src
RUN bash ./enable_kernel_sources.sh
RUN apt-get update && apt-get install -y software-properties-common

# Get the ROS PPA
RUN echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list && \
    wget http://packages.ros.org/ros.key -O - | apt-key add -

# install ros
RUN apt-get -y update && \
    apt-get install -y \
    ros-melodic-desktop-full

# Install the ros packages
RUN apt-get install -y \
    python-catkin-tools \
    python-rosdep \
    python-rosinstall \
    python-rospkg \
    python-wstool \
    ros-melodic-audio-common \
    ros-melodic-catkin \
    ros-melodic-cmake-modules \
    ros-melodic-control-toolbox \
    ros-melodic-gazebo-ros-control \
    ros-melodic-gazebo-ros-pkgs \
    ros-melodic-joint-state-publisher \
    ros-melodic-joy \
    ros-melodic-kdl-parser \
    ros-melodic-moveit \
    ros-melodic-moveit-core \
    ros-melodic-octomap \
    ros-melodic-octomap-msgs \
    ros-melodic-octomap-rviz-plugins \
    ros-melodic-ompl \
    ros-melodic-openni-* \
    ros-melodic-pcl-conversions \
    ros-melodic-realtime-tools \
    ros-melodic-robot-state-publisher \
    ros-melodic-ros-control \
    ros-melodic-ros-controllers \
    ros-melodic-tf-conversions \
    ros-melodic-tf-conversions \
    ros-melodic-robot-self-filter \
    ros-melodic-xacro \
    ros-melodic-tf2-bullet \
    ros-melodic-realtime-tools

RUN pip install rospkg rosdep

RUN rosdep init


####################################################
#             ROS2 INSTALLATION
####################################################

# Setup Local.
RUN apt-get install -y locales
RUN locale-gen en_US en_US.UTF-8
RUN update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
RUN export LANG=en_US.UTF-8

# Setup Sources.
RUN apt update && sudo apt install -y curl gnupg2 lsb-release
RUN curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
RUN sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
RUN apt update

# Install common python packages.
RUN apt update && sudo apt install -y \
  python-rosdep \
  python3-vcstool \
  wget
# install some pip packages needed for testing
RUN python3 -m pip install -U \
  rosdep \
  colcon-common-extensions `# colcon super build tool` \
  argcomplete \
  flake8 \
  flake8-blind-except \
  flake8-builtins \
  flake8-class-newline \
  flake8-comprehensions \
  flake8-deprecated \
  flake8-docstrings \
  flake8-import-order \
  flake8-quotes \
  pytest-repeat \
  pytest-rerunfailures \
  pytest `# colcon optional dep, python unit tests` \
  pytest-cov \
  pytest-runner \
  setuptools `# colcon optional dep, build python package`
# install Fast-RTPS dependencies
RUN apt install --no-install-recommends -y \
  libasio-dev \
  libtinyxml2-dev
# install Cyclone DDS dependencies
RUN apt install --no-install-recommends -y \
  libcunit1-dev

#
# Dashing
#
RUN apt install -y ros-dashing-desktop `# All ROS2 base code.` \
                   ros-dashing-ament-cmake-nose `# Python unit-tests.` \
                   ros-dashing-turtlesim  `# For the DGM tutorial`
