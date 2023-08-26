# ----------
# Option 1
# ----------
s = "Wonderful"

if len(s) < 6:
    print("")
else:
    new_string = s[:3] + s[len(s)-3:]
    print(new_string)

# ----------
# Option 2
# ----------
s = "Wonderful"
num_chars = 3

if len(s) < 6:
    print("")
else:
    new_string = s[:num_chars] + s[len(s)-num_chars:]
    print(new_string)
