# [BASH IGNORE]

FROM ubuntu:20.04
MAINTAINER Vincent Berenz <vincentberenz@tuebingen.mpg.de>

# making sure no prompt during installation
ENV DEBIAN_FRONTEND=noninteractive

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
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install apt-utils


########################################################
# Install basic download tools
########################################################
RUN apt-get update
RUN apt-get -y install curl # command line tool for transferring data with URL syntax
RUN apt-get -y install wget # command line tool for retrieving files using HTTP, HTTPS, FTP and FTPS

########################################################
# Enabling kernel sources
########################################################
# this is necessary for the ros package librealsense in 16.04 (and maybe 18.04 ?)
RUN apt-get install -y sudo              # Provide the sudo rights, required for the enable_kernel_sources.sh script file below
RUN wget -O enable_kernel_sources.sh http://bit.ly/en_krnl_src
RUN bash ./enable_kernel_sources.sh
RUN apt-get update && apt-get install -y software-properties-common
 


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

# seems that killall does not exists in ubuntu18.04
RUN apt-get install -y psmisc

# Potentially just os tools, e.g. editor, fancy terminals
RUN apt-get install -y bash-completion     `# Allow bash completion`\
    	    	       #alien               `# File conversions`\
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
		       #libcairo2-dev       `# 2D Graphics package`\
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
		       #libgirepository1.0-dev   `# Inspect GObject.`\
		       #libpango1.0-dev          `# Police rendering`\
		       m4                       `# a macro processing language`\
		       mesa-utils               `# Miscellaneous Mesa GL utilities`

# # Apollo
# RUN apt-get install -y libgoogle-glog-dev    `# library that implements application-level logging`\
#     	    	       libhdf5-dev           `# Hierarchical Data Format 5`\
# 		       libgflags-dev         `# commandline flags module for C++ (headers)`\
# 		       libgflags2.2          `# commandline flags module for C++ (lib)`\
# 		       liblua5.1-0-dev       `# Development files for the Lua language`\
# 		       luarocks              `# Development files for the Lua language`\
# 		       libxdg-basedir-dev    `# Implementation of the XDG Base Directory Specifications `\
# 		       protobuf-compiler     `# messages formatting package`\
# 		       protobuf-c-compiler   `# messages formatting package`
# 		       #libeinspline-dev      `# library for interpolating cubic basis splines` -> not available on 18.04 ?

# # SL code dependencies
# RUN apt-get install -y libdbus-1-dev         `# SL: shared memory.`\
#     	    	       libc6-dev             `# SL: Linux develpment header files (SL/Xenomai dependencies?)`\
# 		       libedit-dev           `# SL?: Library to edit file (most probably the .cf files) `\
# 		       libccd-dev            `# SL?: collision detection library`\
# 		       libevent-dev          `# SL?: Asynchronous event notification library `\
# 		       libglew-dev           `# SL?: OpenGL Extension Wrangler`\
# 		       libssl-dev            `# SL?: Secure Sockets Layer toolkit`\  
# 		       libstartup-notification0-dev     `# SL?: library for program launch feedback `\
# 		       #libwxgtk3.0-0v5              `# SL?: simulator? wxWidgets Cross-platform C++ GUI toolkit `\ |-> not available on 18.04 ?
# 		       #libwxgtk3.0-0v5-dbg          `# SL?: simulator? wxWidgets Cross-platform C++ GUI toolkit `\ |
# 		       libwxgtk3.0-dev              `# SL?: simulator? wxWidgets Cross-platform C++ GUI toolkit  `\
# 		       libx11-xcb-dev               `# SL?: simulator? Xlib/XCB interface library`\
# 		       libxcb-cursor-dev            `# SL?: simulator? X library `\
# 		       libxcb-icccm4-dev            `# SL?: simulator? X library`\
# 		       libxcb-keysyms1-dev          `# SL?: simulator? X library`\
# 		       libxcb-randr0-dev            `# SL?: simulator? X library`\
# 		       libxcb-render-util0-dev      `# SL?: simulator? X library`\
# 		       libxcb-shape0-dev            `# SL?: simulator? X library`\
# 		       libxcb-util0-dev             `# SL?: simulator? X library `\
# 		       libxcb-xinerama0-dev         `# SL?: simulator? X library`\
# 		       libxcb-xkb-dev               `# SL?: simulator? X library`\
# 		       libxcb-xtest0-dev            `# SL?: simulator? X library`\
# 		       libxcb1-dev                  `# SL?: simulator? X library`\
# 		       libxinerama-dev              `# SL?: simulator? X library`\
# 		       libxkbcommon-dev             `# SL?: simulator? X library`\
# 		       libxkbcommon-x11-dev         `# SL?: simulator? X library`\
# 		       libxmu-dev                   `# SL?: simulator? X library`\
# 		       xutils-dev                   `# SL?: X window utils`\
# 		       net-tools                    `# SL: The NET-3 networking toolkit`\
# 		       ntp                          `# Network Time Protocol daemon and utility programs  `\
# 		       ntpdate                      `# Network Time Protocol daemon and utility programs  `\
# 		       libace-dev                   `# C++ network programming framework - development files`

# Code dependencies 
RUN apt-get install -y autoconf               `# Used to build SNOPT from source`\
		    cmake                  `# C++, Python Project builder`\
		    lsb-release            `# Linux Standard Base version reporting utility `\
		    libconfig++-dev       `# pkgconfig`\
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
		    libslicot-dev          `# SNOPT: numerical algorithms from systems and control theory`\
		    libslicot0             `# SNOPT: numerical algorithms from systems and control theory`\
		    libncurses5-dev        `# Shell management library`\
            libzmq3-dev            `# ZeroMQ for communication over network `\
		    #python-dev             `# python stuff `\
		    #python-netifaces       `# python stuff `\     
		    #python-pip             `# python stuff `\
		    #python-vcstools        `# python stuff `\   
		    #python-wstool          `# python stuff `\
		    #python-qt4             `# python stuff `\
		    #python-empy            `# python stuff `\
		    #python-opencv          `# python stuff `\
		    libcereal-dev          `# serialization library, used in the shared_memory ` \
                    libzmq3-dev            `# ZeroMQ for communication over network ` \
                    xterm                  `# Spawning terminal with gdb via ros2 launch` \
		    ffmpeg            	   `# Extract videos from pybullet ` \
                    libgtest-dev \
		    libboost-dev \
		    libboost-thread-dev 
# docker does not seem to be happy with ffmpeg
# RUN apt-get install -y ffmpeg `# Extract videos from pybullet ` 


#[BASH UPDATE]

############################
# remove unrequired packages
############################
RUN apt-get -y update && apt-get -y upgrade 
RUN apt-get -y autoremove


# Basic packages required for running python3 with catkin setup.
RUN apt-get install -y python3-pip
RUN sudo -H pip3 install --no-cache-dir --upgrade pip
RUN sudo -H pip3 install --no-cache-dir --upgrade \
    catkin_pkg \
    rospkg

RUN sudo -H pip3 install --no-cache-dir  --upgrade \
    empy `Used by ROS in order to generate messages` \
    colorama \
    mock `# for unit testing` \
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
    gcovr `# Compute the code coverage` \
    bs4 `# Install the BeautifulSoup (html parsing)` \
    pybullet `# This the python bindings over the Bullet simulator` \
    #roboball2d `# 2d simulated tennis robot` \
    doxypypy `# Python file parser that create doxygen friendly output` \
    sphinx `# build documentation based on ReStructuredText` \
    m2r `# sphinx module for mardown` \
    recommonmark `# sphinx module for mardown` \
    breathe `# sphinx module for doxygen` \
    sphinxcontrib-moderncmakedomain `# sphinx module for read-the-doc theme` \
    sphinx-rtd-theme `# sphinx module for read-the-doc theme`

# Auto complete treep
RUN sudo activate-global-python-argcomplete

#############################
# setting python3 as default 
#############################

RUN update-alternatives --install /usr/bin/python python /usr/bin/python2 10
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 20

##########################
# installing python2 mock 
##########################

# for reason I do not understand, for CI on Bamboo mock needs to
# be also installed for python2

RUN python2.7 -m pip install mock


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


###############
# Final upgrade
###############
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
