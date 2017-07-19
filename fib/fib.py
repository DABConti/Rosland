f = open("rosalind_fib.txt")

for line in f:
	data = line.split()
	
	n = int(data[0])
	k = int(data[1])
	print n, k
	
rabbitPairs = 1
month = 1
seq = [0]
while month <= n:
	if (month == 1 or month == 2):
		rabbitsN = 1
		seq.append(1)
		print 'Rabbits at month '+str(month) + ': ' + str(rabbitsN)
	else:
		rabbitsN = seq[month-1] + seq[month-2]*3
		seq.append(rabbitsN)
		print 'Rabbits at month '+str(month) + ': ' + str(rabbitsN)
	month +=1
	
	
