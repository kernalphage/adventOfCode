def areaSlack((h,w,l)):
	a = h*w
	b = w*l
	c = l*h
	slack  = min(a, min(b,c))
	return 2 * a + 2 * b + 2 * c + slack
def ribbon((h,w,l)):
	volume = h*w*l
	a = 2*(h + w)
	b = 2*(w + l)
	c = 2*(l + h)
	slack  = min(a, min(b,c))
	return volume + slack;

total =0
rTotal = 0;
with open("input/input2.txt") as f:
	for line in f:
		total += areaSlack( map(int, line.split("x")) ) 
		rTotal += ribbon( [int(x) for x in line.split("x")] ) 

print ("Paper: ",total)
print ("ribbon: ",rTotal)