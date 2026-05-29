#!/usr/bin/env python3
'''
Author ID: 178127239
Author: Jeremy Hernandez
Date: 2025-05-28
'''

def is_digits(sobj):
    # place code here - loop through each character in sobj 
    for char in sobj:
        if not char == '0' and not char == '1' and not char == '2' and not char == '3' and not char == '4' and not char == '5' and not char == '6' and not char == '7' and not char == '8' and not char == '9':
            return False
    return True
if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')