s = "Hello World"

words_list = s.split(" ")
new_s = ""

for word in words_list:
	reversed_word = "".join(reversed(word))
	swapped_case = reversed_word.swapcase()
	new_s += swapped_case + " "

new_s.rstrip()

print(new_s)