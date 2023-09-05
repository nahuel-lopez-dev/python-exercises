# ----------------
# Option 1
# ----------------
is_prime = True

num = int(input("Enter an integer: "))

if num == 0 or num == 1:
	is_prime = False
else:
	for i in range(2, num):
		if num % i == 0:
			is_prime = False
			break

if is_prime:
	print("Prime")
else:
	print("Not Prime")

# ----------------
# Option 2
# ----------------
num = int(input("Enter an integer: "))

if num == 0 or num == 1:
	print("Not Prime")
else:
	for i in range(2, num):
		if num % i == 0:
			print("Not Prime")
			break
	else:
		print("Prime")