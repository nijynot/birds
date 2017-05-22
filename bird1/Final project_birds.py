# -*- coding: utf-8 -*-
"""
Created on Thu May 18 10:34:12 2017
@author: Filipp Lernbo
"""
from  scipy import *
from  pylab import *
from  sys import *
from datetime import datetime
import csv
import pytz
import tzlocal

In_and_out_data=[]
Date=[]
Time=[]

def birdfile(): 
	file = open('birddata.txt', 'r')
	return file
birds1 = list(birdfile())

def splitfunc(birddata):
    moveslist=[]
    datetimelist=[]
    for i in birddata:
        splits = i.split('.')
        datetimelist.append(splits[0])
        splits2 = i.split('   ')
        moveslist.append(int(splits2[1]))
    return datetimelist, moveslist

def make_datetime(dateortimelist):
    local_timezone=tzlocal.get_localzone()
    
    localtz_datetimelist=[]
    for i in dateortimelist:   
        utc_time=datetime.strptime(i, '%Y-%m-%d %H:%M:%S')
        local_time=utc_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)        
        localtz_datetimelist.append(local_time)
    return localtz_datetimelist


#dates=make_datetime(splitfunc(birds1)[0])
#time=make_datetime(splitfunc(birds1)[1])

#print(splitfunc(birds1)[0])
print(make_datetime(splitfunc(birds1)[0])[0])
print(splitfunc(birds1)[0][0])
#print(decimalremover_time(splitfunc(birds1)[0])[0])