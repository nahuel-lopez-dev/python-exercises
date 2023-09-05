n = int(input("Enter the value of 'n': "))

print(f"===== Multiplication Table of {n} =====")

for i in range(1, 11):
	print(f"{n} x {i} = {n * i}")