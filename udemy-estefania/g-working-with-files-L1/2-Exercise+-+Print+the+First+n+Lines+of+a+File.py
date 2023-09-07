file_path = "basic_file.txt"

n = int(input("How many lines would you like to read?: "))

with open(file_path) as file:
	lines = file.readlines()
	num_lines = len(lines)

	if num_lines < n:
		print(f"Please enter a valid value. The file has {num_lines} lines.")
	else:
		for i in range(n):
			print(lines[i].strip("\n"))

