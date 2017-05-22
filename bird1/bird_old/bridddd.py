# -*- coding: utf-8 -*-
"""
Created on Mon May 16 12:30:52 2016

@author: Viktor
"""

def birdfile(): 
	
	file = open('bird1_1.txt', 'r')
	return file

birds1 = list(birdfile())

print (birds1[0], birds1[-1])