def largestPrimeFactor(x):

	largestPrimeFactor = 0
	for i in range(2, x):
		if x % i == 0:
			largestPrimeFactor = i
			print (i)

	return largestPrimeFactor

print (largestPrimeFactor(600851475143))