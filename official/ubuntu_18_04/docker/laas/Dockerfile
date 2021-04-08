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
RUN apt-get -y update --fix-missing
RUN apt-get -y install -f
RUN apt-get -y upgrade

# Install the packages.
#######################

# Gepetto viewer.
RUN apt-get install -y robotpkg-py36-qt5-gepetto-viewer-corba # LAAS 3D robot viewer network client/server.

# Pinocchio
RUN apt-get install -y robotpkg-hpp-fcl               # collision detection for pinocchio.
RUN apt-get install -y robotpkg-libccd                # not sure.
RUN apt-get install -y robotpkg-octomap               # not sure.
RUN apt-get install -y robotpkg-pinocchio             # Eigen based rigid body dynamics library.

# TSID
RUN apt-get install -y robotpkg-parametric-curves           # Spline and polynomes library.
RUN apt-get install -y robotpkg-simple-humanoid-description # Simple humanoid robot_properties package.
RUN apt-get install -y robotpkg-eigen-quadprog              # QP solver using eigen.
RUN apt-get install -y robotpkg-tsid                        # Andrea Delprete Task Space Inverse Dynamics.

# Stack of Tasks (SoT)
RUN apt-get install -y robotpkg-dynamic-graph-v3         # Dynamic graph.
RUN apt-get install -y robotpkg-sot-core-v3              # Stack of Tasks.
RUN apt-get install -y robotpkg-sot-tools-v3             # Dynamic Graph Utilities, to be removed at some point.
RUN apt-get install -y robotpkg-sot-dynamic-pinocchio-v3 # DG wrapper around pinocchio
# RUN apt-get install -y robotpkg-sot-torque-control       # Andrea dynamic graph entities

# A bunch of URDF for the unit-tests
RUN apt-get install -y robotpkg-example-robot-data      # Data for LAAS unnitests.

RUN apt-get install -y robotpkg-py36-tsid                     # python bindings
RUN apt-get install -y robotpkg-py36-dynamic-graph-v3         # python bindings
RUN apt-get install -y robotpkg-py36-eigenpy                  # Python bindings
RUN apt-get install -y robotpkg-py36-pinocchio                # Python bindings
RUN apt-get install -y robotpkg-py36-parametric-curves        # Python bindings
RUN apt-get install -y robotpkg-py36-sot-core-v3              # Python bindings
RUN apt-get install -y robotpkg-py36-quadprog                 # Python bindings
# RUN apt-get install -y robotpkg-py36-sot-torque-control     # Python bindings
RUN apt-get install -y robotpkg-py36-sot-dynamic-pinocchio-v3 # Python bindings

# Install the setup.bash for that detup the environment variables
RUN echo "#! /bin/bash" > /opt/openrobots/setup.bash
RUN echo "" >> /opt/openrobots/setup.bash
RUN echo "export PATH=\"/opt/openrobots/bin:\$PATH\"" >> /opt/openrobots/setup.bash
RUN echo "export PKG_CONFIG_PATH=\"/opt/openrobots/lib/pkgconfig:\$PKG_CONFIG_PATH\"" >> /opt/openrobots/setup.bash
RUN echo "export LD_LIBRARY_PATH=\"/opt/openrobots/lib:\$LD_LIBRARY_PATH\"" >> /opt/openrobots/setup.bash
RUN echo "export LD_LIBRARY_PATH=\"/opt/openrobots/lib/dynamic-graph-plugins:\$LD_LIBRARY_PATH\"" >> /opt/openrobots/setup.bash
RUN echo "export PYTHONPATH=\"/opt/openrobots/lib/python3.6/site-packages:\$PYTHONPATH\"" >> /opt/openrobots/setup.bash
RUN echo "export ROS_PACKAGE_PATH=\"/opt/openrobots/share:\$ROS_PACKAGE_PATH\"" >> /opt/openrobots/setup.bash
RUN echo "export CMAKE_PREFIX_PATH=\"/opt/openrobots:\$CMAKE_PREFIX_PATH\"" >> /opt/openrobots/setup.bash

RUN chown -R root:root /opt/openrobots
