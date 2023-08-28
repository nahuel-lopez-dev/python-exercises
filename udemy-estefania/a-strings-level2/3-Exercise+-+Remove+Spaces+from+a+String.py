# -------------------
# Option 1
# -------------------
s = "Hello, World!"
new_s = ""

for char in s:
	if char != " ":
		new_s += char

print(new_s)

# -------------------
# Option 2
# -------------------
s = "Hello, World!"

print(s.replace(" ", ""))