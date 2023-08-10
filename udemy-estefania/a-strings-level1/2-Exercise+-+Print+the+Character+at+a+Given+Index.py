# -----------
# Option 1
# -----------
s = "Hello"
i = 0

if len(s) == 0:
    print("Empty String")
elif i < len(s):
    print(s[i])
else:
    print("i out of range")

# -----------
# Option 2
# -----------
s = "Hello"
i = 0

if not s:
    print("Empty String")
elif i < len(s):
    print(s[i])
else:
    print("i out of range")


