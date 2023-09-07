file_path = "famous_quotes.txt"
copy_path = "famous_quotes_copy.txt"

with open(file_path) as file, open(copy_path, "w") as copy:
	for line in file:
		copy.write(line)