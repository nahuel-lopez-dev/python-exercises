n = int(input("Enter the value of 'n': "))

factorial = 1

for i in range(2, n+1):
	factorial *= i

print(factorial)