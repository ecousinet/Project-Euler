def isPalindrome(s):
	isPalindrome = True

	for i in range(len(s) // 2):
		if s[i] != s[-(i+1)]:
			isPalindrome = False

	return isPalindrome

largestPalindrome = 0

for i in range(0, 1000):
	for j in range(0, 1000):
		if isPalindrome(str(i*j)):
			if i*j > largestPalindrome:
				largestPalindrome = i*j

print (largestPalindrome)
