#!/usr/bin/env python3
# Author ID: 178127239

import subprocess
p = subprocess.Popen([
    "df -h | grep '/$' | awk '{print $4}'"], 
    stdout=subprocess.PIPE, 
    stdin=subprocess.PIPE, 
    stderr=subprocess.PIPE, 
    shell=True
    )
output, Error = p.communicate()
def free_space():
    space = output.decode('utf-8').strip()
    return space 
print(free_space())