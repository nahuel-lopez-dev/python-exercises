file_path = "words.txt"

longest_word = ""

with open(file_path) as file:
	for word in file:
		if len(word) > len(longest_word):
			longest_word = word

print(longest_word)
