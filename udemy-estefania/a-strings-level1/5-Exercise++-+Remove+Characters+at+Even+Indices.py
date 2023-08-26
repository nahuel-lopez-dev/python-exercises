# -----------
# Option 1
# -----------
s = "Coding"
new_s = ""

for i in range(len(s)):
    if i % 2 != 0:
        new_s += s[i]

print(new_s)

# -----------
# Option 2
# -----------
s = "Coding"
new_s = ""

for i in range(1, len(s), 2):
    new_s += s[i]

print(new_s)
