import os,traceback,sys


class _Mode :

    def __init__(self,tag_open,tag_close):

        self._tag_open = tag_open
        self._tag_close = tag_close
        self._mode_on = False
        
    def update(self,line,line_nb,end=False):

        tag_open = (self._tag_open in line)
        tag_close = (self._tag_close in line)

        if tag_open and tag_close :
            raise Exception("opening and closing tag on the same line is not supported, line "+str(line_nb))
        
        if self._mode_on and tag_close:
            self._mode_on = False
            return

        if (not self._mode_on) and tag_open:
            self._mode_on = True
            return

        if self._mode_on and tag_open:
            raise Exception("invalid tag opening: the tag was already open ( "+str(self._tag_open)+", line "+str(line_nb)+")")

        if (not self._mode_on) and tag_close:
            raise Exception("invalid tag closing: the tag was not open ( "+str(self._tag_close)+", line "+str(line_nb)+")")

        if end and self._mode_on:
            raise Exception("invalid tag: an opening tag ("+str(self._tag_open)+") has never been closed")
        
    def get(self):
        
        return self._mode_on


    
        
def convert_dockerfile_to_bash(dockerfile_path,destination_path,update_only):

    with open(dockerfile_path,"r") as f: content = f.readlines()

    script = ["#! /bin/bash\n\n"]

    bash_ignore_mode = _Mode("[BASH IGNORE]","[/BASH IGNORE]")

    if update_only:
        update_mode = _Mode("[BASH UPDATE]","[/BASH UPDATE]")
    
    
    for line_number,line in enumerate(content):

        if line_number == (len(content)-1):
            end = True
        else:
            end = False
        
        line = line.strip()

        bash_ignore_mode.update(line,line_number,end=end)
        is_bash_ignore = bash_ignore_mode.get()
        
        if update_only:
            update_mode.update(line,line_number,end=end)
            is_update = update_mode.get()

        if not line.startswith("#"):
            
            if not is_bash_ignore:

                if line.startswith("RUN"):
                    line = line[4:]

                if update_only:
                    if is_update:
                        script.append(line)

                else :
                    script.append(line)
        
            
    script_str = "\n".join(script)

    with open(destination_path,"w+") as f :
        f.write(script_str)

    return 

    

    

