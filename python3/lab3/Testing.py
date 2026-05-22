#!/usr/bin/python3
import os

import subprocess

p = subprocess.Popen(
    ["df -h | grep '/$' | awk '{print $4}'"],
    stdout=subprocess.PIPE,
    stdin=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True
)

output= p.communicate()  # unpack the tuple

def free_space():
    space = output[0].decode('utf-8').strip()
    return space

available_space = free_space()
print(available_space)