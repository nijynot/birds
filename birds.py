# -*- coding: utf-8 -*-
"""
Created on Sat May 20 19:38:01 2017

@author: 1048596
"""

import numpy as np
from datetime import datetime, timezone
import copy

def str_to_datetime(date):
    #data = ' '.join(date_str.split()).split() # trim whitespace
    #date_str = data[0] + ' ' + data[1] # concat
    return datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')

def preprocess_line(line):
    data = ' '.join(line.split()).split() # trim whitespace
    print(data)
    timestamp = str_to_datetime(data[0] + ' ' + data[1])
    timestamp = timestamp.replace(tzinfo=timezone.utc).astimezone(tz=None)
    return [timestamp, int(data[2])]

def fix_errors(data):
    new = copy.copy(data)
    for i in range(len(data)):
        if (i == 0):
            new[i][1] = 0
        elif(data[i][1] - data[i - 1][1] > 0):
            print(data[i], data[i - 1])
            new[i][1] = data[i][1] - data[i - 1][1]
        elif(data[i][1] - data[i - 1][1] < 0):
            new.pop(i)
        elif(data[i][1] - data[i - 1][1] == 0):
            new[i][1] = 0
    return new

data = []

with open('bird_jan25jan16.txt', 'r') as f:
    for line in f:
        data.append(preprocess_line(line))