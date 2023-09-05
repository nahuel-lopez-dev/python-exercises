# -------------
# Option 1
# -------------
s = "Hello"

for char in s[::-1]:
	print(char, end="")

# -------------
# Option 2
# -------------
s = "Hello"

for char in reversed(s):
	print(char, end="")

# -------------
# Option 3
# -------------
s = "Hello"

for i in reversed(range(len(s))):
	print(s[i], end="")

# -------------
# Option 4
# -------------
s = "Hello"

for i in range(len(s)-1, -1, -1):
	print(s[i], end="")