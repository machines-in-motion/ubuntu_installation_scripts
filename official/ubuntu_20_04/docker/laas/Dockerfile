# [BASH IGNORE]

FROM docker.is.localnet:5000/amd/18.04:ros
MAINTAINER Vincent Berenz <vincentberenz@tuebingen.mpg.de>

# [/BASH IGNORE]

# Install robotpkg dependencies and other dependencies for dynamic graph
########################################################################

#[BASH UPDATE]

# Add the robotpkg ppa. This contains the LAAS laboratory code base.
# Typically: pinocchio, dynamic-graph, gepetto-viewer, sot-core, ...
RUN echo "deb [arch=amd64] http://robotpkg.openrobots.org/wip/packages/debian/pub $(lsb_release -sc) robotpkg" > /etc/apt/sources.list.d/robotpkg-openrobots.list
RUN echo "deb [arch=amd64] http://robotpkg.openrobots.org/packages/debian/pub $(lsb_release -sc) robotpkg" >> /etc/apt/sources.list.d/robotpkg-openrobots.list
RUN curl http://robotpkg.openrobots.org/packages/debian/robotpkg.key | sudo apt-key add -

# Update the apt list.
RUN apt -y update

# Install the packages.
#######################

# Pinocchio
RUN apt install -y robotpkg-py38-pinocchio
RUN apt install -y robotpkg-py38-crocoddyl

# A bunch of URDF for the unit-tests
RUN apt install -y robotpkg-example-robot-data      # Data for LAAS unnitests.

# Install the setup.bash for that detup the environment variables
RUN echo "#! /bin/bash" > /opt/openrobots/setup.bash
RUN echo "" >> /opt/openrobots/setup.bash
RUN echo "export PATH=\"/opt/openrobots/bin:\$PATH\"" >> /opt/openrobots/setup.bash
RUN echo "export PKG_CONFIG_PATH=\"/opt/openrobots/lib/pkgconfig:\$PKG_CONFIG_PATH\"" >> /opt/openrobots/setup.bash
RUN echo "export LD_LIBRARY_PATH=\"/opt/openrobots/lib:\$LD_LIBRARY_PATH\"" >> /opt/openrobots/setup.bash
RUN echo "export PYTHONPATH=\"/opt/openrobots/lib/python3.8/site-packages:\$PYTHONPATH\"" >> /opt/openrobots/setup.bash
RUN echo "export ROS_PACKAGE_PATH=\"/opt/openrobots/share:\$ROS_PACKAGE_PATH\"" >> /opt/openrobots/setup.bash
RUN echo "export CMAKE_PREFIX_PATH=\"/opt/openrobots:\$CMAKE_PREFIX_PATH\"" >> /opt/openrobots/setup.bash

RUN chown -R root:root /opt/openrobots

#[/BASH UPDATE]