floor = 0
instruction = 0
firstEnter = True
with open("input/input1.txt") as f:
	for c in f.read():
		instruction +=1
		if c=="(":
			floor = floor + 1
		if c==")":
			floor = floor - 1
			if(floor == -1 and firstEnter):
				firstEnter = False
				print("entered basement at ", instruction)

print floor