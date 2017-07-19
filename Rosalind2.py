f = open("rosalind_rna.txt")
g = open("output.txt","w")
for line in f:
		string = line.replace("T","U")
		
print string
g.write(string)

