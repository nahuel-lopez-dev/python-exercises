# -----------
# Option 1
# -----------
s = "Hello"
prefix = "He"

print(s[:len(prefix)] == prefix)

# -----------
# Option 2
# -----------
s = "Hello"
prefix = "He"

print(s.startswith(prefix))
