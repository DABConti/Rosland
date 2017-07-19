f = open("rosalind_hamm.txt")

lines = []

for line in f:
	lines.append(line)
	
strA = lines[0]
strB = lines[1]

print strA
print strB

hammDis = 0


assert len(strA) == len(strB)

for i in xrange(len(strA)):
	if strA[i] != strB[i]:
		hammDis +=1
		
print hammDis
	
