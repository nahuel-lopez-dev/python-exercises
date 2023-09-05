# -------------
# Option 1
#-------------
n = int(input("Enter the value of 'n': "))

for i in range(n, 0, -1):
	print(i)

# -------------
# Option 2
#--------------
n = int(input("Enter the value of 'n': "))

for i in reversed(range(1, n+1)):
	print(i)
