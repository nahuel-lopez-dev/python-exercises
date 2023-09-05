num_rows = int(input("Enter the number of rows: "))

for i in range(num_rows):
	print(chr(65 + i) * (i + 1))