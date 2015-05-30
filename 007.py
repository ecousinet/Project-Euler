def isPrime(x):

	if x % 2 == 0:
		return False
	for i in range(2, x):
		if x % i == 0:
			return False
	return True

i = 1
j = 2
while i <= 10000:	
	if isPrime(j):
		print ("%d: %d" % (i, j))
		i += 1
	j += 1
