# -*- coding: utf-8 -*-
"""
Created on Tue Aug 08 19:31:04 2017
@author: user
"""

lines = 0
FileName = input('Input file name \n')
print(FileName)
for line in open(FileName, 'r'):
    lines += 1
print(lines)