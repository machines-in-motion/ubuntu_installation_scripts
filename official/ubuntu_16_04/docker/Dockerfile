# [BASH IGNORE]

FROM ubuntu:16.04
MAINTAINER Vincent Berenz <vincentberenz@tuebingen.mpg.de>

###################################################################################
# This Dockerfile is also used to generate the official image install ssh 
# script. (see desktop_update folder in amd-clmc/official_images)
# The [BASH IGNORE*]  [/BASH IGNORE*] ; [SSH ONLY*] [/SSH ONLY*] tags are here to indicate
# what will go in the official ssh install script and what will not
###################################################################################

# [/BASH IGNORE]

##########################################################
# Clean the apt cache to always have up to date packages #
##########################################################
RUN apt-get clean
RUN apt-get update
RUN apt-get upgrade

###############################################################################
# We add all other repositories.
###############################################################################

########################################################
# Install basic download tools
########################################################
RUN apt-get update
RUN apt-get -y install curl # command line tool for transferring data with URL syntax
RUN apt-get -y install wget # command line tool for retrieving files using HTTP, HTTPS, FTP and FTPS

####################################################
# Install Git and Git Large File Storage: git-lfs
# (use here for installation of CUDA, for example)
####################################################
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash

RUN apt-get -y update && \
    apt-get install -y \
    git-lfs \
    git-svn

RUN git lfs install --skip-smudge && \
    git config --global credential.helper cache && \
    git config --global credential.helper 'cache --timeout=3600'

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

# !!! does not work on docker, without clear error message
#RUN apt-get install -y \
#    ros-kinetic-turtlebot-* 

RUN rosdep init

###################################################################################################
# Install robotpkg dependencies and other dependencies for dynamic graph
###################################################################################################

#[BASH UPDATE]
# Add the robotpkg ppa. This contains the LAAS laboratory code base.
# Typically: pinocchio, dynamic-graph, gepetto-viewer, sot-core, ...
RUN echo "deb [arch=amd64] http://robotpkg.openrobots.org/wip/packages/debian/pub $(lsb_release -sc) robotpkg" > /etc/apt/sources.list.d/ros-latest.list
RUN echo "deb [arch=amd64] http://robotpkg.openrobots.org/packages/debian/pub $(lsb_release -sc) robotpkg" >> /etc/apt/sources.list.d/ros-latest.list
RUN curl http://robotpkg.openrobots.org/packages/debian/robotpkg.key | sudo apt-key add -

# Install the packages

RUN apt-get -y update --fix-missing

RUN apt-get install -y robotpkg-dynamic-graph-v3      # The dynamic graph
RUN apt-get install -y robotpkg-py27-dynamic-graph-v3 # The dynamic graph python bindings
RUN apt-get install -y robotpkg-tsid                  # Andrea Delprete Task Space Inverse Dynamics
RUN apt-get install -y robotpkg-gepetto-viewer        # LAAS 3D robot viewer

RUN apt-get install -y robotpkg-pinocchio             # Eigen based rigid body dynamics library
RUN apt-get install -y robotpkg-hpp-fcl               # collision detection for pinocchio
RUN apt-get install -y robotpkg-libccd                # not sure
RUN apt-get install -y robotpkg-octomap               # not sure
RUN apt-get install -y robotpkg-parametric-curves     # Spline and polynomes library
RUN apt-get install -y robotpkg-simple-humanoid-description # Simple humanoid robot_properties package
RUN apt-get install -y robotpkg-eigen-quadprog        # QP solver using eigen

RUN apt-get install -y robotpkg-sot-core-v3              # Dynamic Graph Utilities
RUN apt-get install -y robotpkg-sot-tools-v3             # Dynamic Graph Utilities
RUN apt-get install -y robotpkg-sot-dynamic-pinocchio-v3 # DG wrapper around pinocchio
# RUN apt-get install -y robotpkg-sot-torque-control       # Andrea dynamic graph entities

RUN apt-get install -y robotpkg-example-robot-data      # Data for LAAS unnitests.

RUN apt-get install -y robotpkg-py27-eigenpy            # Python bindings
RUN apt-get install -y robotpkg-py27-pinocchio          # Python bindings
RUN apt-get install -y robotpkg-py27-parametric-curves  # Python bindings
RUN apt-get install -y robotpkg-py27-sot-core-v3        # Python bindings
RUN apt-get install -y robotpkg-py27-quadprog           # Python bindings
# RUN apt-get install -y robotpkg-py27-sot-torque-control # Python bindings
RUN apt-get install -y robotpkg-py27-sot-dynamic-pinocchio-v3 # Python bindings
RUN apt-get install -y robotpkg-py27-qt4-gepetto-viewer-corba # LAAS 3D robot viewer network client/server


# Install the setup.bash for that detup the environment variables
RUN echo "#! /bin/bash" > /opt/openrobots/setup.bash
RUN echo "" >> /opt/openrobots/setup.bash
RUN echo "export PATH=\"/opt/openrobots/bin:\$PATH\"" >> /opt/openrobots/setup.bash
RUN echo "export PKG_CONFIG_PATH=\"/opt/openrobots/lib/pkgconfig:\$PKG_CONFIG_PATH\"" >> /opt/openrobots/setup.bash
RUN echo "export LD_LIBRARY_PATH=\"/opt/openrobots/lib:\$LD_LIBRARY_PATH\"" >> /opt/openrobots/setup.bash
RUN echo "export LD_LIBRARY_PATH=\"/opt/openrobots/lib/plugin:\$LD_LIBRARY_PATH\"" >> /opt/openrobots/setup.bash
RUN echo "export PYTHONPATH=\"/opt/openrobots/lib/python2.7/site-packages:\$PYTHONPATH\"" >> /opt/openrobots/setup.bash
RUN echo "export ROS_PACKAGE_PATH=\"/opt/openrobots/share:\$ROS_PACKAGE_PATH\"" >> /opt/openrobots/setup.bash


RUN chown -R root:root /opt/openrobots

################################################################################
# Git Large File Storage: git-lfs (use here for installation of CUDA, for example)
################################################################################
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 6B05F25D762E3157


###################################################################################################
#                              BIG HUGE MESS :)
#
# under ubuntu 16.04 the following changes are made:
# -instead of libwxgtk2.8-dev /-dbg, the following packages are installed:
# 	libwxgtk3.0-0v5
# 	libwxgtk3.0-0v5-dbg
# 	libwxgtk3.0-dev
# -libccd-dev is now installed from apt-get instead of adding the repository to sources.list.d
# -libglew-dev instead of liblew1.6-dev
# -libfcl-dev
# 
# the following repositories are no longer supported under 16.04:
# fcl-debs
# libccd-debs
# however, the libraries are intalled with apt-get
##################################################################################################

# here we update once before all the apt-get install
RUN apt-get -y update

# Potentially just os tools, e.g. editor, fancy terminals
RUN apt-get install -y bash-completion     `# Allow bash completion`\
    	    	       alien               `# File conversions`\
		       terminator          `# Fancy terminal`\
		       apt-file            `# Is a software package that indexes`\
                                           `# the contents of packages in your`\
                                           `# available repositories and allows you`\
                                           `# to search for a particular file among`\
                                           `# all available packages.`\
		       autofs              `# Used to automount external device (usb, HD, ...)`\
		       bc                  `# "JrBc", A calculator that can be used from the command-line`\
		       imagemagick         `# Image manipulation (convert)`\
		       f2c                 `# Fortran to C/C++ translator`\
		       libf2c2-dev         `# To be used with f2c (fortran 2 c/c++)`\
		       man                 `# on-line manual pager`\
		       libcairo2-dev       `# 2D Graphics package`\
		       patch               `# Apply a diff file to an original`\
		       picocom             `# minimal dumb-terminal emulation program`\
		       rpm                 `#  Tools to create and apply deltarpms`\
		       scons               `# replacement for make, depends on python... ????`\
		       screen              `# terminal multiplexer with VT100/ANSI terminal emulation`\
		       shellcheck          `# lint tool for shell scripts`\
		       vim                 `# Terminal editor`\
		       swig                `# Generate scripting interfaces to C/C++ code`\
		       tcsh                `# TENEX C Shell, an enhanced version of Berkeley csh`\
		       xmlto               `# XML-to-any converter`

# Development tools
RUN apt-get install -y less                `# Similar to "more", installed by default?`\
                       ccache              `# Optimize the cache during build.`\
                       gdb                 `# code debugger`\
                       iputils-ping        `# Tools to test the reachability of network hosts`\
                       cmake-curses-gui    `# ccmake`\
                       ssh                 `# ssh client+server`\
                       openssh-server      `# ssh server`\
                       sshpass             `# Non-interactive ssh password authentication`\
                       emacs               `# Basic text editor`

# Code dependencies ?
RUN apt-get install -y asciidoc                 `# "Highly configurable text format for writing documentation"`\
    	    	       libffi-dev               `# Code binder developped by Haskell`\
		       libgirepository1.0-dev   `# Inspect GObject.`\
		       libpango1.0-dev          `# Police rendering`\
		       m4                       `# a macro processing language`\
		       mesa-utils               `# Miscellaneous Mesa GL utilities`

# Apollo
RUN apt-get install -y libgoogle-glog-dev    `# library that implements application-level logging`\
    	    	       libhdf5-dev           `# Hierarchical Data Format 5`\
		       libgflags-dev         `# commandline flags module for C++ (headers)`\
		       libgflags2v5          `# commandline flags module for C++ (lib)`\
		       liblua5.1-0-dev       `# Development files for the Lua language`\
		       luarocks              `# Development files for the Lua language`\
		       libxdg-basedir-dev    `# Implementation of the XDG Base Directory Specifications `\
		       protobuf-compiler     `# messages formatting package`\
		       protobuf-c-compiler   `# messages formatting package`\
		       libeinspline-dev      `# library for interpolating cubic basis splines`

# SL code dependencies
RUN apt-get install -y libdbus-1-dev         `# SL: shared memory.`\
    	    	       libc6-dev             `# SL: Linux develpment header files (SL/Xenomai dependencies?)`\
		       libedit-dev           `# SL?: Library to edit file (most probably the .cf files) `\
		       libccd-dev            `# SL?: collision detection library`\
		       libevent-dev          `# SL?: Asynchronous event notification library `\
		       libglew-dev           `# SL?: OpenGL Extension Wrangler`\
		       libssl-dev            `# SL?: Secure Sockets Layer toolkit`\  
		       libstartup-notification0-dev     `# SL?: library for program launch feedback `\
		       libwxgtk3.0-0v5              `# SL?: simulator? wxWidgets Cross-platform C++ GUI toolkit `\
		       libwxgtk3.0-0v5-dbg          `# SL?: simulator? wxWidgets Cross-platform C++ GUI toolkit `\
		       libwxgtk3.0-dev              `# SL?: simulator? wxWidgets Cross-platform C++ GUI toolkit  `\
		       libx11-xcb-dev               `# SL?: simulator? Xlib/XCB interface library`\
		       libxcb-cursor-dev            `# SL?: simulator? X library `\
		       libxcb-icccm4-dev            `# SL?: simulator? X library`\
		       libxcb-keysyms1-dev          `# SL?: simulator? X library`\
		       libxcb-randr0-dev            `# SL?: simulator? X library`\
		       libxcb-render-util0-dev      `# SL?: simulator? X library`\
		       libxcb-shape0-dev            `# SL?: simulator? X library`\
		       libxcb-util0-dev             `# SL?: simulator? X library `\
		       libxcb-xinerama0-dev         `# SL?: simulator? X library`\
		       libxcb-xkb-dev               `# SL?: simulator? X library`\
		       libxcb-xtest0-dev            `# SL?: simulator? X library`\
		       libxcb1-dev                  `# SL?: simulator? X library`\
		       libxinerama-dev              `# SL?: simulator? X library`\
		       libxkbcommon-dev             `# SL?: simulator? X library`\
		       libxkbcommon-x11-dev         `# SL?: simulator? X library`\
		       libxmu-dev                   `# SL?: simulator? X library`\
		       xutils-dev                   `# SL?: X window utils`\
		       net-tools                    `# SL: The NET-3 networking toolkit`\
		       ntp                          `# Network Time Protocol daemon and utility programs  `\
		       ntpdate                      `# Network Time Protocol daemon and utility programs  `\
		       libace-dev                   `# C++ network programming framework - development files`

# Code dependencies 
RUN apt-get install -y autoconf               `# Used to build SNOPT from source`\
		    cmake                  `# C++, Python Project builder`\
		    lsb-release            `# Linux Standard Base version reporting utility `\
		    libconfig++8-dev       `# pkgconfig`\
		    binutils               `# GNU assembler, linker and binary utilities`\
		    build-essential        `# Build tools (gcc, g++, ...)`\
		    gfortran               `# Fortran compiler`\
		    doxygen                `# Main documentation writting used`\
		    freeglut3              `# OpenGL Utility Toolkit`\
		    freeglut3-dev          `# OpenGL Utility Toolkit`\
		    libblas-dev            `# Basic Linear Algebra Subroutines 3, static library `\
		    liblapack-dev          `# Linear algebra subroutines`\
		    libarmadillo-dev       `# Linear algebra and scientific computing`\
		    libeigen3-dev          `# Linear Algebra header library`\
		    libfcl-dev             `# flexible collision library`\
		    libslicot-dbg          `# SNOPT: numerical algorithms from systems and control theory`\
		    libslicot-dev          `# SNOPT: numerical algorithms from systems and control theory`\
		    libslicot0             `# SNOPT: numerical algorithms from systems and control theory`\
		    libncurses5-dev        `# Shell management library`\
		    python-dev             `# python stuff `\
		    python-netifaces       `# python stuff `\     
		    python-pip             `# python stuff `\
		    python-vcstools        `# python stuff `\   
		    python-wstool          `# python stuff `\
		    python-qt4             `# python stuff `\
		    python-empy            `# python stuff `\
		    python-opencv
#[/BASH UPDATE]

###############################################################################
# PYTHON MODULES
# new for 16.04:
# pip first has to be installed with apt-get
###############################################################################


#[BASH UPDATE]
RUN apt-get install -y python-pip
RUN sudo -H pip2 install --no-cache-dir --upgrade pip
RUN sudo -H pip2 install --no-cache-dir  pyopenssl
RUN sudo -H pip2 install --no-cache-dir  --upgrade \
    colorama \
    matplotlib `# Plotting library` \
    seaborn \
    ndg-httpsclient \
    numpy `# Linear algebra library` \
    pyasn1 \
    schedule \
    scipy \
    sklearn \
    virtualenv `# Creation of virtual environment for python2` \
    appdirs \
    h5py \
    keras \
    ipython `# Nice python terminal` \
    ipdb \
    jupyter `# Nice python web interface` \
    treep `# MPI-IS code project manager` \
    sphinx `# Python documentation generator` \
    gcovr `# Compute the code coverage` \
    bs4 `# Install the BeautifulSoup (html parsing)`

RUN sudo -H pip2 install --no-cache-dir pydot==1.0.28
RUN sudo -H pip2 install --no-cache-dir pyparsing==2.0.1
RUN sudo -H pip2 install --no-cache-dir --upgrade six --target="/usr/lib/python2.7/dist-packages"
RUN sudo -H pip2 install --no-cache-dir appdirs
RUN sudo -H pip2 install --no-cache-dir --upgrade protobuf
RUN sudo -H pip2 install --no-cache-dir --upgrade sphinx

# Basic packages required for running python3 with catkin setup.
RUN apt-get install -y python3-pip
RUN sudo -H pip3 install --no-cache-dir --upgrade pip
RUN sudo -H pip3 install --no-cache-dir --upgrade \
    catkin_pkg \
    rospkg 
RUN sudo -H pip3 install --no-cache-dir --upgrade sphinx

# Auto complete treep
RUN sudo activate-global-python-argcomplete

#[/BASH UPDATE]

#############################################################################
# Software Workshop RAI
#############################################################################
# !!! this requires some more configuration, see
# readme.txt for docker clues (works on 14.04, need update for 16.04)
# note : the commands below requires access to DNS, for docker configuration
#        check the readme.txt file in the same folder as this Dockerfile
#[BASH UPDATE]
#RUN cd /tmp && \
#    wget --no-check-certificate https://code.is.localnet/media/artifacts/AMD%20plotting%20library/89163d92f9ee40a10dc76762946babc4/RAI-0.3.tar.gz && \
#    tar -xzf ./RAI-0.3.tar.gz && \
#    cd RAI-0.3 && \
#    sudo -H pip install .
#[/BASH UPDATE]

###############################################################################
# required for the use of snopt 
###############################################################################
#[BASH UPDATE]
RUN wget http://ftp.gnu.org/gnu/autoconf/autoconf-2.69.tar.gz -P /tmp/ && \
    tar -xf /tmp/autoconf-2.69.tar.gz -C /tmp/ && \
    rm /tmp/autoconf-2.69.tar.gz && \
    cd /tmp/autoconf-2.69 && \
    ./configure && \
    make -C /tmp/autoconf-2.69 && \
    make install -C /tmp/autoconf-2.69
#[/BASH UPDATE]

#[BASH IGNORE]
#########################################
# for convenience, to map workspace in it
#########################################
RUN mkdir /workspace
RUN mkdir /ssh
#[/BASH IGNORE]

#[BASH IGNORE]
############################################
# creating a user for continuous integration
############################################
RUN useradd -p $(openssl passwd -1 bamboo) bamboo
RUN usermod -aG sudo bamboo
#[/BASH IGNORE]

############################
# remove unrequired packages
############################
RUN apt-get -y update && apt-get -y upgrade 
RUN apt-get -y autoremove
#[BASH UPDATE]
RUN apt-get -y update && apt-get -y upgrade  
#[/BASH UPDATE]

########################
# start ssh agent
########################
RUN eval `ssh-agent -s`

##########################################################
# Clean the apt cache to always have up to date packages #
##########################################################
RUN apt-get clean
