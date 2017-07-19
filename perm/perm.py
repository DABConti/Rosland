import itertools

n = 7
seq = []
output = 0
for i in xrange(n):
	seq.append(i)
	
perms = itertools.permutations(range(n))
permsNew = []

for perm in perms:
	tmp = ''
	for num in perm:
		tmp+=str(num+1)+' '
	tmp = tmp.strip()
	permsNew.append(tmp)
	

print len(permsNew)
for part in permsNew:
	print part
	
