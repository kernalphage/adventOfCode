
slurps = 0 
writes = 0
raw = ""
bloat =""

with open("input/input8.txt") as f:
	for line in f:
		raw = raw + line.strip();
		bloat+='"'
		for c in line.strip():
			if c == '"' or c == '\\':
				bloat += "\\"
			bloat += c
		bloat += '"'

print bloat

rawLen = len(raw)
packed = ""
i = 0
#decode
while i < rawLen:
	c = raw[i]
	i+=1
	if c == '"':
		pass
	elif c == '\\':
		peek = raw[i]
		i+=1
		if(peek == '\\'):
			packed += '\\'
		elif(peek == '"'):
			packed += '"'
		elif(peek == 'x'):
			i+=2
			packed += 'x'
	else:
		packed+=c


print rawLen
print len(packed)
print (rawLen - len(packed))
print len(bloat) - rawLen