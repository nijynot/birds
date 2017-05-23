# -*- coding: utf-8 -*-
"""
Created on Sat May 20 19:38:01 2017
 
@author: 1048596
"""
 
import numpy as np
from datetime import datetime, timezone, timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import matplotlib.ticker as ticker
 
def preprocess_line(line):
    data = ' '.join(line.split()).split() # trim whitespace
    date = data[0] + ' ' + data[1]
    timestamp = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f').replace(tzinfo=timezone.utc).astimezone(tz=None)
    return [timestamp, int(data[2])]

def diff(data):
    new = []
    for i in range(len(data)):
        delta = data[i][1] - data[i - 1][1]
        if (delta > 100):
            print(delta, i)
        if (data[i][1] == 0 and data[i + 1][1] - data[i - 1][1] >= 0):
            data[i][1] = int((data[i - 1][1] + data[i + 1][1]) / 2)
        elif (i == 0 or data[i][1] == 0):
            new.append([data[i][0], 0])
        elif (delta >= 0):
            new.append([data[i][0], np.clip(delta, 0, 5)])
        elif (delta < 0):
            data[i][1] = int((data[i - 1][1] + data[i + 1][1]) / 2)
            #count = data[i - 1][1]
            new.append([data[i][0], new[-1][1]])
    return new

def filter_by_interval(data, lower, upper):
    dates = []
    for i in range(len(data)):
        if (data[i][0] > lower and data[i][0] < upper):
            dates.append(data[i])
    return dates

def sum_score(data, lower, upper):
    score = 0
    for i in range(len(data)):
        if (data[i][0] > lower and data[i][0] < upper):
            score += data[i][1]
    return score

def reduce(data):
    new = []
    tmp = list(data)
    while len(tmp) > 0:
        print(len(tmp))
        lower_hour = tmp[0][0].replace(minute=0, second=0, microsecond=0)
        upper_hour = lower_hour + timedelta(hours=1)
        score = sum_score(data, lower_hour, upper_hour)
        tmp = [line for line in tmp if line[0] > upper_hour]
        new.append([upper_hour, score])
    return new

def plot(data):
    x = [line[0] for line in data]
    y = [line[1] for line in data]
    fig, ax = plt.subplots()
    fig.autofmt_xdate()
    ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    ax.bar(x, y, width=0.1, facecolor='b', alpha=.5, linewidth=0)
    plt.show()

data = []
 
date1 = datetime.strptime('2015-03-01', '%Y-%m-%d').replace(tzinfo=timezone.utc).astimezone(tz=None)
date2 = datetime.strptime('2015-03-04', '%Y-%m-%d').replace(tzinfo=timezone.utc).astimezone(tz=None)

fig, ax = plt.subplots(1)
#fig.autofmt_xdate()
plt.plot([date1, date2], [13, 5])

xfmt = dates.DateFormatter('%H')
ax.xaxis.set_major_formatter(xfmt)

plt.show()

with open('sample.txt', 'r') as f:
    for line in f:
        data.append(preprocess_line(line))

data = diff(data)
data = reduce(data)
filterd = filter_by_interval(data, date1, date2)