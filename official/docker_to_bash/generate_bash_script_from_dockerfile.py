import os,traceback,sys
import docker_to_bash

UBUNTU_14_04 = "14_04"
UBUNTU_16_04 = "16_04"
UBUNTU_18_04 = "18_04"

# there are several dockerfiles which can be used
# to generates a bash script, all in ubuntu_xx_x/dockerfile
# managing this (several dockerfiles can be used to run a
# single installation script)
# users choices are :
# "core"     -> core
# "ros"      -> core + ros
# "laas"     -> core + laas
# "utils"    -> core + utils
# "all-code" -> core + ros + laas
# "all"      -> core + ros + laas + utils
# continuous integration will be run on "all-code"
CORE = "core" # core code dependencies
ROS = "ros" # ros packages
LAAS = "laas" # dynamic graph , pinocchio, etc
UTILS = "utils" # not code dependencies (e.g. latex, ide, etc)
OPTIONS = { "core"     : [CORE],
            "ros"      : [CORE,ROS] ,
            "laas"     : [CORE,LAAS],
            "utils"    : [CORE,UTILS],
            "all-code" : [CORE,ROS,LAAS],
            "all"      : [CORE,ROS,LAAS,UTILS] }

MODE_FULL = 1
MODE_UPDATE_ONLY = 2


def _get_ubuntu_version():
    
    if "14.04" in sys.argv:
        return UBUNTU_14_04
    if "16.04" in sys.argv:
        return UBUNTU_16_04
    if "18.04" in sys.argv:
        return UBUNTU_18_04
    raise Exception("14.04 or 16.04 or 18.04 should be passed as argument")


def _get_this_script_directory():

    full_path = os.path.realpath(__file__)
    basename = os.path.basename(full_path)
    path = full_path[:-len(basename)]
    return os.path.abspath(path)


def _get_mode():

    if "install" in sys.argv:
        return MODE_FULL
    if "update" in sys.argv:
        return MODE_UPDATE_ONLY
    raise Exception("install or update should be passed as argument")


class _OptionException(Exception):
    pass

def _get_options():

    global OPTIONS

    for option in OPTIONS.keys():
        if option in sys.argv:
            return OPTIONS[option]

    error_message = ["pass as argument the desired installation:"]
    error_message.append("\tcore: minimal code dependencies")
    error_message.append("\tros: core + ros and selected ros packages")
    error_message.append("\tlaas: core + dynamic graph and other laas packages")
    error_message.append("\tutils: tools, e.g. latex or IDEs")
    error_message.append("\tall-code: core + laas + ros")
    error_message.append("\tall: core + laas + ros + utils")

    raise _OptionException("\n".join(error_message))
    

def _execute():

    ubuntu_version = _get_ubuntu_version()

    # installing from scratch or
    # just updating
    mode = _get_mode()
    if mode == MODE_FULL:
        update_only=False
    else :
        update_only=True

    # which set to install ? e.g. core, ros, laas
    options = _get_options()
        
    directory_path = _get_this_script_directory()

    destination_path = os.path.abspath(directory_path+os.sep+".."+os.sep+"tmp"+os.sep)
    if not os.path.isdir(destination_path):
        try : os.makedirs(destination_path)
        except Exception as e :
            raise Exception ("Failed to create "+destination_path+": "+str(e))

    destination_file = destination_path+os.sep+"tmp_install_file"
    if os.path.isfile(destination_file):
        try: os.remove(destination_file)
        except Exception as e :
            raise Exception ("Failed to remove "+destination_file+": "+str(e))
 
    full_script = []
        
    for option in options:
    
        path_to_dockerfile = os.sep.join([directory_path,
                                          "..",
                                          "ubuntu_"+ubuntu_version,
                                          "docker",
                                          option,
                                          "Dockerfile"])
        path_to_dockerfile = os.path.abspath(path_to_dockerfile)
        
        if not os.path.isfile(path_to_dockerfile): 
            raise Exception("Failed to find: "+path_to_dockerfile)

        try : script = docker_to_bash.convert_dockerfile_to_bash(path_to_dockerfile,
                                                                 update_only)
        except Exception as e :
            print("")
            traceback.print_exc()
            print("")
            raise Exception("Failed to convert dockerfile into bashfile: "+str(e))

        full_script.append(script)
        
    with open(destination_file,"w+") as f :
        f.write("\n".join(full_script))


if __name__ == "__main__" : 

    try:
        _execute()
    except _OptionException as e:
        print(e)
    except Exception as e:
        print("")
        traceback.print_exc()
        print("")
        print("[ERROR]\n"+str(e)+"\n")
        print("contact vberenz@tuebingen.mpg.de for debug (copy/paste trace above)")
        print
