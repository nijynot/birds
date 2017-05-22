# -*- coding: utf-8 -*-
"""
Created on Sun May 22 17:19:59 2016

@author: Viktor
"""
from datetime import datetime, date, timedelta
import numpy as np
import matplotlib.dates as dates

from scipy import *
from pylab import *
import sys
import scipy.special
import numpy as np
import matplotlib.pyplot as pyp
from datetime import datetime
import pytz		
import tzlocal # pip install tzlocal

"""Birds fix av feldata"""
def birdfile(): 
	file = open('bird1_1.txt', 'r')
	return file
birds1 = list(birdfile())
#print (birds1[0], birds1[-1])

def splitfunc(birddata):
	moves = []
	dates = []
	for i in birddata:
		splits = i.split('   ')
		dates.append(splits[0])
		splits2 = i.split()
		moves.append(int(splits2[2]))
	return dates, moves
	
diffar = []	
def movesfix(movesarr, x):
	"""korrigerar array of moves till maxantal x"""
	movesdiff = diff(movesarr)
	moveslist = [0]
	for i in movesdiff:
		if i >= x:
			moveslist.append(x)
			diffar.append(i)
		elif i < 0:
			moveslist.append(median(movesdiff))
			diffar.append(i)
		else:
			moveslist.append(i)
	return moveslist
	
muves = movesfix(asarray(splitfunc(birds1)[1]), 8)
#print('max:', max(muves))
#print('antal diffar:', len(diffar))
#print(len(muves))
#print(sum(muves))

def tz_fix(ymd):
	"""ändrar till lokal tidszon"""
	datum = []
	local_timezone = tzlocal.get_localzone() # get pytz tzinfo
	for n in ymd:
		utc_time = datetime.strptime(n, "%Y-%m-%d %H:%M:%S.%f")
		local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)
		datum.append(local_time)
	return datum	

def findday(data, month, day):
	"""hittar ett visst datum i listan baserat på månad och dag"""
	daily = []
	for i in data:	
		if str(month)+'-'+str(day) in i:
			daily.append(i)
	return daily
#femmars = findday(birds1, '03', '05')
#print('femte mars 2015:',femmars[0])

def findintrvl(data, start, stop):
	"""hittar och listar begärda datum. väldigt långsam. datum anges som 'mm-dd'."""
	intrvl = []
	a = []
	for i in data:
		if str(start) in i:
			a.append(data.index(i))
			break
	for j in data:
		if str(stop) in j:
			a.append(data.index(j))
			break
	for n in data:
		if data.index(n) in range(a[0], a[-1]):
			intrvl.append(n)
	return intrvl

def daysum(rawdata, startdate, stopdate):
	"""här vill jag skriva kod som appendar moves till en lista per dag.
	funktionen skall returnera sum(lista) för samtliga listor
	lite oklart hur det ska gå till bara"""
	sumlist = []
	
"""kodanrop som ger plot, datumet kan bytas efter önskemål"""
#datum = findintrvl(birds1, '03-04', '03-08')
#print(datum[0])
#a = splitfunc(datum)
#x = tz_fix(a[0])
#print(x[0:4])
#y = movesfix(a[1], 8)

#print('starttime:', x[0], 'antal tider:', len(x))
#print('startvalue:', y[0], 'antal moves:', len(y), 'max moves:', max(y))

#dates = plt.dates.date2num(x)
#plot_date(dates, y, ('r'))


def findmonth(data, year, month):
	"""hittar ett visst datum i listan baserat på månad och dag"""
	monthly = []
	for i in data:	
		if str(year)+'-'+str(month) in i:
			monthly.append(i)
	return monthly
fmars = findmonth(birds1, '2015', '03')
print('mars 2015:',fmars[0])

datum = findintrvl(birds1, '03-01', '03-25')
print(datum[0])
b = splitfunc(fmars)
xm = tz_fix(b[0])
#print(y[0:4])
ym = movesfix(b[1], 8)

c=splitfunc(fmars)
xmz=tz_fix(c[0])
ymz=movesfix(c[1], 8)

#print('starttime:', x[0], 'antal tider:', len(x))
#print('startvalue:', y[0], 'antal moves:', len(y), 'max moves:', max(y))


#datesm = matplotlib.dates.date2num(xm)
#plot_date(datesm, ym, ('r'))

from matplotlib.dates import WeekdayLocator

def plot_series(xmz, ymz):
    fig, ax = plt.subplots()
    ax.plot_date(xmz, ymz, fmt='g') # x = array of dates, y = array of numbers        

    fig.autofmt_xdate()

 

    # For tickmarks (no ticklabel) every week
    ax.xaxis.set_minor_locator(WeekdayLocator(byweekday=MO))

    # Grid for both major and minor ticks
    plt.grid(True, which='both')
    plt.show()

hej = plot_series(xmz, ymz)
print(hej)    




#from matplotlib import pyplot as plt
#xmval=[xm]
#y=[ym]
#x=range(len(xmval))
#plt.xticks(x,xval)
#plt.plot(xm,ym)
#plt.show()





