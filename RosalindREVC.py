f = open("rosalind_revc.txt")

outStr = ""

for line in f:
	for char in line:
		if char == "A":
			outStr +="T"
		if char == 'C':
			outStr +="G"
		if char == 'G':
			outStr +="C"
		if char == 'T':
			outStr +="A"
			
print outStr[::-1]
