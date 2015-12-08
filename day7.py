import re
class EvalNode:
	"""An eval node"""
	def __init__(self, name):
		self.name = name;
		self.cached = -1

	def parse(self):
		if(self.cached == -1):
			#print("parsing", self.name)
			self.cached = applyOp(self.l.parse(), self.op, self.r.parse())
		return self.cached;

class ConstNode:
	def __init__(self, const):
		self.const = const;
		self.name = str(const)
	def parse(self):
		return self.const

def applyOp(l, op, r):
	if op == "NOT":
		return ~r
	elif op == "AND":
		return l & r
	elif op == "OR":
		return l | r
	elif op == "LSHIFT":
		return l << r
	elif op == "RSHIFT":
		return l >> r
	#const
	else:
		return r;
		
#empty strings are matched, yes. We want them to be evaluated to 0
re_isConst = re.compile("\d*$")
def isConst(str):
	return re_isConst.match(str);

def parseLine(line):
	args = line.strip().split(" ")
	args.reverse()
	args += [''] * (5 - len(args))
	(out, arrow, right, op, left) = args;
	#print(out, " = ", left, op, right )
	if(isConst(left)):
		l = ConstNode( int('0'+left) )
	else:
		l = wires[left]

	if(isConst(right)):
		r = ConstNode( int('0'+right) )
	else:
		r = wires[right]
	#print(wires[out].name, " = " , l.name, r.name ); 

	wires[out].l = l;
	wires[out].r = r;
	wires[out].op = op;


#build wire list
wires = { "":{} }
for i in range(ord('a'), ord('z')+1):
	wires[chr(i)] = EvalNode(chr(i));
	for j in range(ord('a'), ord('z')+1):
		wires[chr(i)+chr(j)] = EvalNode(chr(i)+chr(j));

#add wire tree
with open("input/input7.txt") as f:
	for line in f:
		parseLine( line );

aay = wires['a'].parse();
print ( aay );

for i in range(ord('a'), ord('z')+1):
	wires[chr(i)].cached = -1
	for j in range(ord('a'), ord('z')+1):
		wires[chr(i)+chr(j)].cached = -1;

wires['b'].cached = aay
print ( wires['a'].parse() );
