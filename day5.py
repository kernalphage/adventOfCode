import re
###part one
def numVowels(str):
	return sum(map(lambda x: str.count(x), "aeiou"))

re_hasDupe = re.compile("(?P<one>.)(?P=one)")
def hasDuplicate(str):
	return bool( re_hasDupe.search(str)) 

def naughtyWord(str):
	matchList = [bool(re.search(x,str)) for x in [ "ab", "cd", "pq", "xy"]];
	return reduce(lambda x,y: x or y, matchList, False)


#### part two
re_hasDupe2 = re.compile("(?P<one>..).*(?P=one)")
def hasDuplicate2(str):
	return bool( re_hasDupe2.search(str)) 

re_hasInside = re.compile("(?P<one>.).(?P=one)")
def hasInside(str):
	return bool( re_hasInside.search(str)) 
nice1 = 0
nice2 = 0
with open("input/input5.txt") as f:
	for line in f:
		if numVowels(line) > 2 and hasDuplicate(line) and not naughtyWord(line):
			nice1 +=1 
		if hasDuplicate2(line) and hasInside(line):
			nice2 +=1

print ("Nice : ", nice1)
print ("Nice2: ", nice2)
