#!/usr/bin/env python3
import sys
print(sys.argv)
if len(sys.argv) != 3:
     print('Usage: ',sys.argv[0])
else:
    name = sys.argv[1]
    age = sys.argv[2]
    print('Name: '+name+ '\nAge: '+age+  '\nHi ' + name + ', you are ' + age + ' years old.')
     
