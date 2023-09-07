file_path = "basic_file.txt"

file_content = []

with open(file_path) as file:
	for line in file:
		file_content.append(line)

print(file_content)