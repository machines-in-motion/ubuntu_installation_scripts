# [BASH IGNORE]

FROM docker.is.localnet:5000/amd/16.04:core
MAINTAINER Vincent Berenz <vincentberenz@tuebingen.mpg.de>

# [/BASH IGNORE]

# snap, for installing some of the packages below
RUN apt install snapd

# Mattermost + support for video calls
RUN snap install riot-web
RUN snap connect riot-web:camera 
RUN snap install mattermost-desktop  

# Install Visual Studio Code editor.
RUN snap install code --classic # Visual studio code editor

