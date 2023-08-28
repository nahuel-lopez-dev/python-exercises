# Test "Hello", "Corporation", "Python"

# -----------------
# Option 1
# -----------------
s = "Hello"

repeated_count = 0
repeated_chars = []

for char in s:
	if (s.count(char) > 1) and (char not in repeated_chars):
		repeated_count += 1
		repeated_chars.append(char)

print(repeated_count)

if len(repeated_chars) > 0:
	for char in sorted(repeated_chars):
		print(char, end=" ")
else:
	print(None)

# -----------------
# Option 2
# -----------------
s = "Hello"

repeated_count = 0
repeated_chars = []

for char in s:
	if (s.count(char) > 1) and (char not in repeated_chars):
		repeated_count += 1
		repeated_chars.append(char)

print(repeated_count)

if repeated_chars: # Use truthy value
	print(*sorted(repeated_chars), sep=" ") # One line, avoid loop
else:
	print(None)

# -----------------------------
# Option 3: Remove count
# -----------------------------
s = "Hello"

repeated_chars = []

for char in s:
	if (s.count(char) > 1) and (char not in repeated_chars):
		repeated_chars.append(char)

print(len(repeated_chars))

if repeated_chars:
	print(*sorted(repeated_chars), sep=" ")
else:
	print(None)
