#!/usr/bin/python3
import os


ls_return = os.system('ls')
print('The contents of ls_return:',ls_return)
whoami_return = os.system('whoami')
print('The contents of whoami_return:',whoami_return)
ifconfig_return = os.system('ifconfig')
print('The contents of ifconfig_return:',ifconfig_return)


'''
ls_return = os.popen('ls')
print('The contents of ls_return:',ls_return)
whoami_return = os.popen('whoami')
print('The contents of whoami_return:',whoami_return)
ifconfig_return = os.popen('ifconfig')
print('The contents of ifconfig_return:',ifconfig_return)

whoami_return=os.popen('whoami')
whoami_contents = whoami_return.read()
print('whoami_contents:',whoami_contents)

ipconfig_return = os.popen('ipconfig')
ipconfig_contents = ipconfig_return.read()
print('The contents of ipconfig_return:',ipconfig_contents)
'''