# -----------
# Option 1
# -----------
s = "Hello"
n = 1

if (len(s) == 0) or (n >= len(s)):
    print(s)
else:
    new_s = ""
    for i in range(len(s)):
        if i != n:
            new_s += s[i]
    print(new_s)


# -----------
# Option 2
# -----------
s = "Hello"
n = 1

if (not s) or (n >= len(s)):
    print(s)
else:
    new_s = ""
    for i in range(len(s)):
        if i != n:
            new_s += s[i]
    print(new_s)
