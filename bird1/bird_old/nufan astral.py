# -*- coding: utf-8 -*-
"""
Created on Thu May 19 14:24:55 2016

@author: Viktor
"""

from scipy import *
from pylab import *
import sys
import scipy.special
import numpy as np
import pandas as pd
import csv


"""Birds"""





def birdfile(): 
	
	file = open('bird1_1.txt', 'r')
	return file
moves = []
dates = []	
birds1 = list(birdfile())

import datetime
#from astral import Astral

Alla_datum= []
new_list= []

for i in birds1:
    splits2= i.split()
    Alla_datum.append(splits2[0])

#for i in Alla_datum:
#    if i not in new_list:
#        new_list.append((i))

#datumz = []
#from datetime import datetime
#import pytz		
#import tzlocal # pip install tzlocal
#def tz_fix(dates):
#	local_timezone = tzlocal.get_localzone() # get pytz tzinfo
#	for n in dates:
#		utc_time = datetime.strptime(n, "%Y-%m-%d")
#		local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)
#		datumz.append(local_time)
#	return datumz
#	lägg till timer?
#	spara till fil?
#x = tz_fix(new_list)
#print(x[0])


#print(new_list[0],new_list[-1])
#print(len(new_list))

#city_name = 'Stockholm'

#a = Astral()
#a.solar_depression = 'civil'

#city = a[city_name]

#print('Information for %s/%s\n' % (city_name, city.region))

#timezone = city.timezone
#print('Timezone: %s' % timezone)


#print('Latitude: %.02f; Longitude: %.02f\n' % \
#        (city.latitude, city.longitude))

#sun = []
#for i in x:
#	sun.append(city.sun(date=datetime.date(i), local=True))

#lista = []
#for i in sun:
#	a = list(i.items())
#	lista.append(a)
#	splits = lista.split()
#print(splits[0])
#print('hej!',lista[0],'hejdå!')

#dawnlist = []
#dusklist = []

#import itertools as it
#light = []
#dawn = []
#dusk = []
#for i in lista:
#	dawn.append(i[3])
#	dusk.append(i[2])
#print(dawn[0])
#for i in dawn:
#	a = list(i)
#	dawnlist.append(a)
#for j in dusk:
#	b = list(j)
#	dusklist.append(b)
#print('hej!',dawnlist[2][1], dusklist[2][1])

#light = list(it.zip_longest(dawnlist, dusklist))
#print('hej', light[0], light[-1])

#print('Dawn:    %s' % str(sun['sunrise']))
#print('Sunrise: %s' % str(sun['sunrise']))
#print('Noon:    %s' % str(sun['noon']))
#print('Sunset:  %s' % str(sun['sunset']))
#print('Dusk:    %s' % str(sun['dusk']))


jan = []
feb = []
mar = []
apr = []
maj = []

for h in range(len(birds1)):
    if birds1[h][6] == '1':
        jan.append(birds1[h])
    elif birds1[h][6] == '2':
        feb.append(birds1[h])
    elif birds1[h][6] == '3':
        mar.append(birds1[h])
    elif birds1[h][6] == '4':
        apr.append(birds1[h])
    elif birds1[h][6] == '5':
        maj.append(birds1[h])

movesjan = []
movesfeb = []
movesmar = []
movesapr = []
movesmaj = []

for n in range(len(jan)-1):
    movesjan.append(movescheck[n])

for n in range(len(feb)-1):
    movesfeb.append(movescheck[(n+len(jan))])

for n in range(len(mar)-1):
    movesmar.append(movescheck[(n+len(jan)+len(feb))])

for n in range(len(apr)-1):
    movesapr.append(movescheck[(n+len(jan)+len(feb)+len(mar))])

for n in range(len(maj)-1):
    movesmaj.append(movescheck[(n+len(jan)+len(feb)+len(mar)+len(apr))])

print(mean(movesjan))
print(mean(movesfeb))
print(mean(movesmar))
print(mean(movesapr))
print(mean(movesmaj))

tfapr = []
for n in range(len(apr)):
    if apr[n][8] == '2':
        if apr[n][9] == '4':
            tfapr.append(apr[n])

print(tfapr)

movestfapr = []
for i in (tfapr):
    splits = i.split()
#    dates.append(splits2)
    movestfapr.append(int(splits[2]))


print(movestfapr)


diffmovestfapr = diff(movestfapr)
print(diffmovestfapr)


#dt = datetime.datetime.now()
#dt = dt.replace(microsecond=0) # Returns a copy
#dt
#datetime.datetime(2015, 4, 24, 0, 0)

#if dt == None : dt = datetime.datetime.now()
#seconds = (dt - dt.min).seconds
# // is a floor division, not a comment on following line:
#rounding = (seconds+roundTo/2) // roundTo * roundTo
#return dt + datetime.timedelta(0,rounding-seconds,-dt.microsecond)

#for k in range(len(tfapr)):
#    tfapr.remove(tfapr[k][19])
#    tfapr.remove(tfapr[k][20])
#    tfapr.remove(tfapr[k][21])
#    tfapr.remove(tfapr[k][22])
#    tfapr.remove(tfapr[k][23])
#    tfapr.remove(tfapr[k][24])
#    tfapr.remove(tfapr[k][25])

#3datetime.datetime(2010, 7, 6, 5, 27, 23, 662390)
#dtwithoutseconds = dt.replace(second=0, microsecond=0)



#print(tfapr)   
#tfaprs = []
#for k in range(len(tfapr)-1):
#    tfaprs.append((tfapr[k].split("<--")[19].split("-->")[25]))

#print(tfaprs)

#http://stackoverflow.com/questions/28765563/average-values-from-a-column-on-an-hourly-timeseries

#import itertools as it
#datumbirds = list(zip(datum, movescheck))
#print(len(datumbirds))
#print('hej!', datumbirds[0], datumbirds[-1])