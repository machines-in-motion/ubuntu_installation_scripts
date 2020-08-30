# [BASH IGNORE]

FROM docker.is.localnet:5000/amd/18.04:core
MAINTAINER Vincent Berenz <vincentberenz@tuebingen.mpg.de>

# [/BASH IGNORE]

####################################################
#             ROS INSTALLATION
####################################################

# Setup Local.
RUN locale-gen en_US en_US.UTF-8
RUN update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
RUN export LANG=en_US.UTF-8

# Setup Sources.
RUN apt update && sudo apt install curl gnupg2 lsb-release
RUN curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -

RUN sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'

# Install ROS 2 packages.
RUN apt update
RUN apt install ros-eloquent-desktop

# Install argcomplete
RUN pip3 install -U argcomplete

# Make sure roskpg is still installed in order to identify package path for config files
RUN pip3 install rospkg