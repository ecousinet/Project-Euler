def isDivisible(dividend, divisor):
	""" Return true if dividend is divisible by divisor """
	if dividend % divisor == 0:
		return True
	else:
		return False

i = 1
while True:
	divisible = True
	for j in range (1, 21):
		if not isDivisible(i, j):
			divisible = False
	if divisible:
		break
	i += 1

print (i)
