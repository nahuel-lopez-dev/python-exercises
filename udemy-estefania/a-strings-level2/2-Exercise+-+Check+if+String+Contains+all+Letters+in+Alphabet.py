# ---------------------
# Option 1
# ---------------------
import string

s = "The quick brown fox jumps over the lazy dog"

set_s = set(s.lower())
set_s.remove(" ")
print(set_s == set(string.ascii_lowercase))

# ---------------------
# Option 2
# ---------------------
import string

s = "The quick brown fox jumps over the lazy dog"
is_pangram = True

for char in string.ascii_lowercase:
    if char not in s.lower():
        is_pangram = False

print(is_pangram)

# ---------------------
# Option 3
# ---------------------
import string

s = "The quick brown fox jumps over the lazy dog"
is_pangram = True

for char in string.ascii_lowercase:
    if char not in s.lower():
        is_pangram = False
        break # Stop the loop immediately

print(is_pangram)