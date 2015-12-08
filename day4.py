import md5
key = "yzbqklnj"
found = [False, False, False, False, False, False, False]

for i in xrange(0,10000000):
	k = key + str(i)
	m = md5.new(k).hexdigest()
	for o in range(1,8):
		if(m.startswith('0'*o)):
			if( not found[o] ):
				found[o] = True, False
				print  i, "\t", o, " zeroes", m
