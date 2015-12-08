from __future__ import print_function
import re
import numpy as np
from matplotlib import pyplot as plt

re_rect = re.compile("[^\d]*(\d*),(\d*) through (\d*),(\d*)")
re_on = re.compile(".*on")
re_off = re.compile(".*off")

lights = np.zeros((1000,1000))

#### part 1 
def turnOn(pt):
	lights[ pt[0],pt[1] ] = 1
 
def turnOff(pt):
	lights[ pt[0],pt[1] ] = 0

def toggle(pt):
	lights[ pt[0],pt[1] ] = (lights[ pt[0],pt[1] ] + 1) % 2

#### part 2
def turnOn2(pt):
	lights[ pt[0],pt[1] ] += 1
 
def turnOff2(pt):
	lights[ pt[0],pt[1] ] = max(0,lights[ pt[0],pt[1] ] - 1)

def toggle2(pt):
	lights[ pt[0],pt[1] ] += 2

def getRect(str):
	grp = re_rect.match(str)
	return [int(x) for x in (grp.groups())]

def fOnRect(f, rect):
	print(f.__name__, rect)
	for x in xrange(rect[0], rect[2]+1):
		for y in xrange(rect[1], rect[3]+1):
			f( (x,y) ) 

def doLine( str ):
	if(re_on.match(str)):
		f = turnOn
	elif(re_off.match(str)):
		f = turnOff
	else:
		f = toggle
	fOnRect(f,getRect(str))


with open("input/input6.txt") as f:
	for line in f:
		doLine(line)

plt.imshow(lights, interpolation='nearest')
plt.show()