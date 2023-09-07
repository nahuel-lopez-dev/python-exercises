file_path = "famous_quotes.txt"

character_count = 0

with open(file_path) as file:
	for line in file:
		character_count += len(line.replace(" ", "").strip("\n"))

print(character_count)