def count_vowels(string):
	string = string.lower()
	if not string:
		return 0
	elif string[0] in ("a", "e", "i", "o", "u"):
		return 1 + count_vowels(string[1:])
	else:
		return count_vowels(string[1:])