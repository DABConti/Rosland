f = open("rosalind_prot.txt")

lines = []

rnaCordon = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
'UAA': 'Stop',   'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
'UAG': 'Stop',   'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
'UGA': 'Stop',   'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G' }


for line in f:
	lines.append(line)
	
seq = lines[0].strip()


print seq

hammDis = 0
output = ''

i=0
print len(seq)
while i < len(seq):
	print i
	subSeq = seq[i] + seq[i+1] + seq[i+2]
	cordon = rnaCordon[subSeq]
	if cordon != 'Stop':
		output += rnaCordon[subSeq]
	i+=3
		
print output
	
