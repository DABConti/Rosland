f = open("rosalind_dna.txt")
a =0
c = 0
g = 0
t = 0
for line in f:
	for char in line:
		print char +" "
		if char == "A":
			a +=1
		if char == 'C':
			c +=1
		if char == 'G':
			g +=1
		if char == 'T':
			t +=1
		
print str(a)+" "+str(c)+" "+str(g)+" "+str(t)
