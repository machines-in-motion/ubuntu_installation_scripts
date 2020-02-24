# [BASH IGNORE]

FROM docker.is.localnet:5000/amd/16.04:core
MAINTAINER Vincent Berenz <vincentberenz@tuebingen.mpg.de>

# [/BASH IGNORE]

####################################################
#             ROS INSTALLATION
##
#under ubuntu 16.04 the following changes are made:
#the following packages don't exist in ros kinetic:
#-driver-common 
#-keyboard
####################################################

# enable kernel sources
# this is necessary for the ros package librealsense in 16.04
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
    ros-kinetic-desktop-full

# Install the ros packages
RUN apt-get install -y \
    python-catkin-tools \
    python-rosdep \
    python-rosinstall \
    python-rospkg \
    python-wstool \
    ros-kinetic-audio-common \
    ros-kinetic-catkin \
    ros-kinetic-cmake-modules \
    ros-kinetic-control-toolbox \
    ros-kinetic-ecto \
    ros-kinetic-gazebo-ros-control \
    ros-kinetic-gazebo-ros-pkgs \
    ros-kinetic-joint-state-publisher \
    ros-kinetic-joy \
    ros-kinetic-kdl-parser \
    ros-kinetic-moveit \
    ros-kinetic-moveit-core \
    ros-kinetic-octomap \
    ros-kinetic-octomap-msgs \
    ros-kinetic-octomap-rviz-plugins \
    ros-kinetic-ompl \
    ros-kinetic-openni-* \
    ros-kinetic-pcl-conversions \
    ros-kinetic-qt-build \
    ros-kinetic-realtime-tools \
    ros-kinetic-robot-state-publisher \
    ros-kinetic-ros-control \
    ros-kinetic-ros-controllers \
    ros-kinetic-tf-conversions \
    ros-kinetic-tf-conversions \
    ros-kinetic-robot-self-filter \
    ros-kinetic-xacro \
    ros-kinetic-tf2-bullet \
    ros-kinetic-realtime-tools 

RUN rosdep init


