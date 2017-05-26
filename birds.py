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
        dbldelta = data[i][1] - data[i - 2][1]
        if dbldelta == 0:
            pass
        elif (delta <= 0):
            pass
        elif (0 < delta < 8 or delta >= 8):
            new.append([data[i][0], np.clip(delta, 0, 8)])
    return new

def diff_astral(data):
    new = []
    for i in range(len(data)):
        delta = data[i][1] - data[i - 1][1]
        if (delta > 100): # check if over 100
            print(delta, i)
        if (data[i][1] == 0 and data[i + 1][1] - data[i - 1][1] >= 0):
            # if count is 0 and row - 1 and row + 1 is non-zero,
            # then set count as average
            data[i][1] = int((data[i - 1][1] + data[i + 1][1]) / 2)
        elif (i == 0 or data[i][1] == 0): # if first row
            new.append([data[i][0], 0])
        elif (delta >= 0): # if positive
            new.append([data[i][0], np.clip(delta, 0, 5)])
        elif (delta < 0): # if negative set average of i - 1 and i + 1
            data[i][1] = int((data[i - 1][1] + data[i + 1][1]) / 2)
            new.append([data[i][0], new[-1][1]])
    return new

def filter_by_interval(data, lower, upper):
    dates = []
    for row in data:
        if (row[0] > lower and row[0] < upper):
            dates.append(row)
    return dates

def sum_score(data, lower, upper):
    score = 0
    for row in data:
        if (row[0] > lower and row[0] < upper):
            score += row[1]
    return score

def reduce(data, type):
    new = []
    tmp = list(data)
    while len(tmp) > 0:
        print(len(tmp))
        lower_hour = tmp[0][0].replace(minute=0, second=0, microsecond=0)
        if (type == 'days'):
            upper_hour = lower_hour + timedelta(days=1)
        elif (type == 'hours'):
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
    #ax.xaxis.set_minor_locator(dates.HourLocator())
    ax.bar(x, y, width=0.05, facecolor='b', alpha=.5, linewidth=0)
    plt.show()

def plot_astral(data):
    a = Astral()
    a.solar_depression = 'civil'
    l = Location(('Södra Sandby', 'Sweden', 55.712163, 13.332234, 'Europe/Copenhagen', 0))
    x = [line[0] for line in data]
    y = [line[1] for line in data]
    #date1 = datetime.strptime('2015-03-02', '%Y-%m-%d').replace(tzinfo=timezone.utc).astimezone(tz=None)
    #date2 = datetime.strptime('2015-03-03', '%Y-%m-%d').replace(tzinfo=timezone.utc).astimezone(tz=None)
    fig, ax = plt.subplots()
    fig.autofmt_xdate()
    ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    ax.xaxis.set_major_locator(dates.DayLocator(bymonthday=range(1,32), interval=1))
    ax.xaxis.set_major_formatter(dates.DateFormatter('%Y-%m-%d'))
    ax.bar(x, y, width=0.05, facecolor='b', alpha=.5, linewidth=0)
    #ax.axvspan(date1, date2, color='y', alpha=.2, linewidth=0)
    for i in range(len(x)):
        ast = l.sun(date=x[i], local=True)
        if (ast['dawn'] < x[i] and ast['dusk'] > x[i]):
            ax.axvspan(x[i], x[i] + timedelta(hours=1), color='y', alpha=.2, linewidth=0)
    plt.show()
    
data = []
 
date1 = datetime.strptime('2015-03-01', '%Y-%m-%d').replace(tzinfo=timezone.utc).astimezone(tz=None)
date2 = datetime.strptime('2015-03-04', '%Y-%m-%d').replace(tzinfo=timezone.utc).astimezone(tz=None)
'''
fig, ax = plt.subplots(1)
#fig.autofmt_xdate()
plt.plot([date1, date2], [13, 5])

xfmt = dates.DateFormatter('%H')
ax.xaxis.set_major_formatter(xfmt)

plt.show()'''

with open('interval.txt', 'r') as f:
    for line in f:
        data.append(preprocess_line(line))

#data_all = diff(data)
#data_all = reduce(data_all, 'days')
data_astral = diff_astral(data)
data_astral = reduce(data_astral, 'hours')
filterd = filter_by_interval(data_astral, date1, date2)