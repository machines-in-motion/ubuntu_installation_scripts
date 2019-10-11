import os,traceback,sys
import docker_to_bash

UBUNTU_14_04 = "14_04"
UBUNTU_16_04 = "16_04"
UBUNTU_18_04 = "18_04"

MODE_FULL = 1
MODE_UPDATE_ONLY = 2


def _get_ubuntu_version():
    
    if "14.04" in sys.argv:
        return UBUNTU_14_04
    if "16.04" in sys.argv:
        return UBUNTU_16_04
    if "18.04" in sys.argv:
        return UBUNTU_18_04
    raise Exception("14.04, 16.04 or 18.04 should be passed as argument")


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
        


def _execute():

    ubuntu_version = _get_ubuntu_version()

    mode = _get_mode()
    if mode == MODE_FULL:
        update_only=False
    else :
        update_only=True
    
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
    
    path_to_dockerfile = directory_path+os.sep+".."+os.sep+"ubuntu_"+ubuntu_version+os.sep+"docker"+os.sep+"Dockerfile"
    path_to_dockerfile = os.path.abspath(path_to_dockerfile)
    if not os.path.isfile(path_to_dockerfile): 
        raise Exception("Failed to find: "+path_to_dockerfile)


    print
    print "creating file",destination_file
    print "from",path_to_dockerfile
    print
    
    try : docker_to_bash.convert_dockerfile_to_bash(path_to_dockerfile,
                                                    destination_file,
                                                    update_only)
    except Exception as e :
        print
        traceback.print_exc()
        print
        raise Exception("Failed to convert dockerfile into bashfile: "+str(e))


if __name__ == "__main__" : 

    try:
        _execute()
    except Exception as e:
        print
        traceback.print_exc()
        print
        print "[ERROR]\n"+str(e)+"\n"
        print "contact vberenz@tuebingen.mpg.de for debug (copy/paste trace above)"
        print
