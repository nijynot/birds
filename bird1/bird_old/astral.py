# -*- coding: utf-8 -*-
"""
Created on Thu May 19 13:51:53 2016

@author: Viktor
"""

def birdfile(): 
	
	file = open('bird1_1.txt', 'r')
	return file
moves = []
dates = []	
birds1 = list(birdfile())

import datetime
from astral import Astral

Alla_datum= []
new_list= []

for i in birds1:
    splits2= i.split()
    Alla_datum.append(splits2[0])

for i in Alla_datum:
    if i not in new_list:
        new_list.append((i))

datumz = []
from datetime import datetime
import pytz		
import tzlocal # pip install tzlocal
def tz_fix(dates):
	local_timezone = tzlocal.get_localzone() # get pytz tzinfo
	for n in dates:
		utc_time = datetime.strptime(n, "%Y-%m-%d")
		local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)
		datumz.append(local_time)
	return datumz
#	lägg till timer?
#	spara till fil?
x = tz_fix(new_list)
print(x[0])


print(new_list[0],new_list[-1])
print(len(new_list))

city_name = 'Stockholm'

a = Astral()
a.solar_depression = 'civil'

city = a[city_name]

print('Information for %s/%s\n' % (city_name, city.region))

timezone = city.timezone
print('Timezone: %s' % timezone)


print('Latitude: %.02f; Longitude: %.02f\n' % \
        (city.latitude, city.longitude))

sun = []
for i in x:
	sun.append(city.sun(date=datetime.date(i), local=True))

lista = []
for i in sun:
	a = list(i.items())
	lista.append(a)
#	splits = lista.split()
#print(splits[0])
print('hej!',lista[0],'hejdå!')

import itertools as it
light = []
dawn = []
dusk = []
dawnlist = []
dusklist = []
for i in lista:
	dawn.append(i[3])
	dusk.append(i[2])
print(dawn[0])
for i in dawn:
	a = list(i)
	dawnlist.append(a)
for j in dusk:
	b = list(j)
	dusklist.append(b)
print('hej!',dawnlist[2][1], dusklist[2][1])

light = list(it.zip_longest(dawnlist, dusklist))
print('hej', light[0], light[-1])

#print('Dawn:    %s' % str(sun['sunrise']))
#print('Sunrise: %s' % str(sun['sunrise']))
#print('Noon:    %s' % str(sun['noon']))
#print('Sunset:  %s' % str(sun['sunset']))
#print('Dusk:    %s' % str(sun['dusk']))