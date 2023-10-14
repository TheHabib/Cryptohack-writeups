from math import sqrt

def isPrime(n):


	if (n <= 1):
		return False
	for i in range(2, int(sqrt(n))+1):
		if (n % i == 0):
			return False

	return True


if __name__ == '__main__':
	x = int(input("Enter the range: "))
	if isPrime(x):
		print("It is prime")
	else:
		while(True):
			x+=1
			if isPrime(x) == True:
				break

	print(f"Your prime is: {x}")
