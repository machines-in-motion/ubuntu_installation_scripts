# [BASH IGNORE]

FROM docker.is.localnet:5000/amd/18.04:core
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
RUN rosdep init


