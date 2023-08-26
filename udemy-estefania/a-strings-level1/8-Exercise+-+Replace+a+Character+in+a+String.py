# -----------
# Option 1
# -----------
s = "Hello"
new_s = ""

curr_char = "l"
new_char = "s"

for char in s:
    if char == curr_char:
        new_s += new_char
    else:
        new_s += char

print(new_s)

# -----------
# Option 2
# -----------
s = "Hello"

curr_char = "l"
new_char = "s"

print(s.replace(curr_char, new_char))

