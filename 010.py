def isPrime(x):
	if x == 1:
		return False
	if x == 2:
		return True
	if x % 2 == 0:
		return False
	for i in range(2, x):
		if x % i == 0:
			return False
	return True

result = 0
for i in range(2000000):
	if isPrime(i):
		result += i

print (result)
