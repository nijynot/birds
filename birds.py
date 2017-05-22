# -*- coding: utf-8 -*-
"""
Created on Sat May 20 19:38:01 2017

@author: 1048596
"""

import numpy as np
from datetime import datetime, timezone
import copy
import matplotlib.pyplot as plt

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
    
def fix_corrupt(data):
    new = []
    for i in range(len(data)):
        diff = data[i][1] - data[i - 1][1]
        if(i == 0):
            new.append([data[i][0], 0])
        elif(diff > 8):
            new.append([data[i][0], 8])
        elif(diff > 0):
            count = data[i][1] - data[i - 1][1]
            new.append([data[i][0], count])
        elif(diff <= 0):
            count = data[i - 1][1]
            new.append([data[i][0], count])
    return new

def plot_hourly(data, date, days):
    dates = []
    for i in range(len(data)):
        if (data[i][0].date() == date):
            dates.append(data[i])

data = []

with open('bird_jan25jan16 copy.txt', 'r') as f:
    for line in f:
        data.append(preprocess_line(line))