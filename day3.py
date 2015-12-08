import collections
Point = collections.namedtuple("Point", 'x y')
pos = Point(0,0)
loc = {pos: 1}
rpos = Point(0,0)
rloc = {rpos: 1}

def dictMergeWithAdd(a,b):
	res = {}
	for i in a.keys():
		res[i] = a[i] + b.pop(i,0)
	for i in b.keys():
		res[i] = b[i]
	return res

instruction = 0
with open("input/input3.txt") as f:
	for c in f.read():
		if(instruction % 2 == 0):
			if c == ">":
				pos = Point(pos.x+1, pos.y)
			if c == "<":
				pos = Point(pos.x-1, pos.y)
			if c == "^":
				pos = Point(pos.x  , pos.y+1)
			if c == "v":
				pos = Point(pos.x  , pos.y-1)
			if( pos not in loc ):
				loc[pos] = 0;
			loc[pos]+=1
		#robot
		else:
			if c == ">":
				rpos = Point(rpos.x+1, rpos.y)
			if c == "<":
				rpos = Point(rpos.x-1, rpos.y)
			if c == "^":
				rpos = Point(rpos.x  , rpos.y+1)
			if c == "v":
				rpos = Point(rpos.x  , rpos.y-1)
			if( rpos not in rloc ):
				rloc[rpos] = 0;
			rloc[rpos]+=1
		instruction+=1


both = dictMergeWithAdd(loc,rloc)
print("Santa", len(loc))
print("Both",  len(both))
