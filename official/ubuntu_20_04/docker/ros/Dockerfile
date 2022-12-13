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
    ros-noetic-desktop-full

# Install the ros packages
RUN apt-get install -y \
    #python-catkin-tools \
    #python-rosdep \
    #python-rosinstall \
    #python-rospkg \
    #python-wstool \
    ros-noetic-audio-common \
    ros-noetic-catkin \
    ros-noetic-cmake-modules \
    ros-noetic-control-toolbox \
    ros-noetic-gazebo-ros-control \
    ros-noetic-gazebo-ros-pkgs \
    ros-noetic-joint-state-publisher \
    ros-noetic-joy \
    ros-noetic-kdl-parser \
    ros-noetic-moveit \
    ros-noetic-moveit-core \
    ros-noetic-octomap \
    ros-noetic-octomap-msgs \
    ros-noetic-octomap-rviz-plugins \
    ros-noetic-ompl \
    ros-noetic-openni-* \
    ros-noetic-pcl-conversions \
    ros-noetic-realtime-tools \
    ros-noetic-robot-state-publisher \
    ros-noetic-ros-control \
    ros-noetic-ros-controllers \
    ros-noetic-tf-conversions \
    ros-noetic-tf-conversions \
    ros-noetic-robot-self-filter \
    ros-noetic-xacro \
    ros-noetic-tf2-bullet \
    ros-noetic-realtime-tools

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
  #python-rosdep \
  python3-vcstool \
  wget
# install some pip packages needed for testing
RUN python3 -m pip install -U \
  rosdep \
  colcon-common-extensions `# colcon super build tool` \
  xacro `# building udrf files` \
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
# Foxy
#
RUN apt install -y ros-foxy-desktop `# All ROS2 base code.` \
                   ros-foxy-ament-cmake-nose `# Python unit-tests.` \
                   ros-foxy-turtlesim  `# For the DGM tutorial`
