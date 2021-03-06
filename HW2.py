import random 

def GetNumber(user_guess):
    if (user_guess.isnumeric()):
        return True
    else:
        print("The number that you have entered is not a valid number.")
        return False

def calculateSum(n) : 
	if (n <= 0) : 
		return 0

	iM2 = 0
	iM1 = 1
	fib = iM2 + iM1

	sm = fib

	while fib < n : 
		iM2 = iM1
		iM1 = fib
		sm = sm + fib 
		fib = iM2 + iM1
		
	return sm 

def isPrime(n) : 

	if (n <= 3) : 
		return n > 1


	# check to skip middle 5 numbers while looping
	if (n % 2 == 0 or n % 3 == 0) : 
		return False

	i = 5
	while(i * i <= n) : 
		if (n % i == 0 or n % (i + 2) == 0) : 
			return False
		i = i + 6

	return True

while True : 
	rawInput = input("Please enter an integer: ")
	if (GetNumber (rawInput)) :
		n  = int(rawInput)
		print("Sum of Fibonacci numbers is : ", calculateSum(n)) 

		print(n, bin(n).replace("0b", "( binary: "), ") is" if isPrime(n) else ") is not" , "a prime number")
		quit() 
 
