#!/bin/bash
#
# Script to install the ukuu program.
#
# See:
#   https://vitux.com/update-linux-kernel-on-ubuntu-through-ukuu/

sudo add-apt-repository ppa:teejee2008/ppa
sudo apt-get update
sudo apt-get install -y ukuu

# sudo ukuu --install v4.19.72

