import base64

print(ord(";") - ord('\''))

line="13-1-19-20-5-18-2-18-1-14-3-8"
print [chr(ord('a') + int(i) - 1) for i in line.split("-")]	

line = "Lzwjw ak s ljwskmjw zavvwf kgewozwjw, al ak dguslwv sl s kwujwl hdsuw af lzw Hsuaxau Guwsf"
for i in range(0,26):
	print "".join([chr(ord('a') + (ord(c) - ord('a') + i) % 26 ) if c is not " " else " " for c in line])

line = "Om s ept;f gi;; pg n;pvld"
for i in range (-26, 26):
	print "".join([chr(ord('!') + (ord(c) - ord('!') - i)  ) if c is not " " else " " for c in line])

print base64.b64decode("VGhlIHBsYW50IGlzIGZhbW91cyBiZWNhdXNlIG9mIHRoZSBhYmlsaXR5IHRvIGN1cmUgc29tZSBkaXNlYXNlcw==")