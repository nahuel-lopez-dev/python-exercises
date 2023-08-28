# -----------
# Option 1
# -----------
s = "Hello"
suffix = "ello"

print(s[-len(suffix):] == suffix)

# -----------
# Option 2
# -----------
s = "Hello"
suffix = "ello"

print(s.endswith(suffix))
