def sumOfXSquare(x):
	result = 0
	for i in range(1, x + 1):
		result += i ** 2
	return result

def squareOfXsum(x):
	result = 0
	for i in range(1, x+1):
		result += i
	return result ** 2

print (squareOfXsum(100) - sumOfXSquare(100))