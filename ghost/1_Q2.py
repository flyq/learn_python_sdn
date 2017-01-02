#!/usr/bin/env python

import base64

filename = raw_input('Enter file name: ')
input_file = open(filename)
input_a = input_file.read()
input_file.close()
    
output_a = base64.b64decode(input_a)
print output_a
