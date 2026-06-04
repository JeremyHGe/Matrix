#!/usr/bin/env python3
# Author ID: 178127239
# Author Name: Jeremy Hernandez

def read_file_string(file_name):
    f = open(file_name, 'r')
    return f.read()

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    f = open(file_name, 'r')
    return list(line.strip() for line in f.readlines())
if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))