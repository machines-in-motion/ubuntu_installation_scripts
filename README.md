The repositories contains convenience installation scripts for ubuntu.

## Installing Ubuntu

The most useful script is official/setup_ubuntu . This script is meant to be called after a fresh installation of ubuntu, and, depending on the argument passed, installs all typical dependencies required for programming robots. These include ROS, dynamic graph and related [robotpkg](http://robotpkg.openrobots.org/) software (e.g stack of task and pinocchio). Call the script without arguments to see the installation options.

**Only Ubuntu16.04 and Ubuntu18.04 are fully supported**. *Ubuntu16.04 support is going to be dropped soon*. The script will also work on 14.04, but this is deprecated and will mostly install ROS and dependencies related to SL will be installed.

Usage:

```bash
cd official
sudo ./setup_ubuntu
# possible arguments are displayed, for example
sudo ./setup_ubuntu install core
```


To see the list of software this script install (and how it install it), visit the related dockerfiles (e.g. for 16.04 : in official/ubuntu_16_04).

## Realtime rt-preempt scripts

In the preempt folder you will also find scripts useful for patching your *Ubuntu16.04* and *Ubuntu18.04* kernel.


## Credits

Authors / Maintainers :

- Vincent Berenz
- Maximilien Naveau
- Julian Viereck
