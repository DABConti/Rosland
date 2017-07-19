f = open("rosalind_gc.txt")
lines = []
dna = ""
for line in f:
	if line[0] == '>':
		if len(dna) > 0:
			lines.append(dna)
			dna = ""
		lines.append(line.strip())
	else:
		dna += line.strip()
	
lines.append(dna)

fasta = {}
gc = {}
maxGC = '0'
maxGCVal = 0
for i in xrange(len(lines)):
	line = lines[i]
	if line[0] == '>':
		fasta[line.strip('>')] = lines[i+1]
		
for key in fasta:
	dnaLen = len(fasta[key])
	gcCount = fasta[key].count('G') + fasta[key].count('C')
	
	gcContent = round(float(gcCount)/float(dnaLen), 8)*100
	
	if gcContent > maxGCVal:
		maxGC = key
		maxGCVal = gcContent
		
print maxGC
print maxGCVal
		


	

