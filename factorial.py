def factorial(num):
	# your code here
	number = 1
	for i in range(1,num+1):
		number = number * i
	return number
print(factorial(4))






# In this exercise you are going to create a function that takes a number parameter and returns the factorial of it.

# Factorial has a very specific definition. Learn more here. As an overview though, a factorial is the result of multiplying a sequence of descending numbers down to 0. Factorials are only defined for non-negative integer numbers. This definition includes zero. Though 0! is equal to 1, so treat it as an edge case.
# factorial(0); // 1
# factorial(1); // 1
# factorial(2); // 2 * 1
# factorial(3); // 3 * 2 * 1
# factorial(4); // 4 * 3 * 2 * 1 = 24
# // ...etc