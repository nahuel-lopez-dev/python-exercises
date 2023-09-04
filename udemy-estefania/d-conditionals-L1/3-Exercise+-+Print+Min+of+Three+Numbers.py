# -------------
# Option 1
# -------------
a = 1
b = 2
c = 3

if (a <= b) and (a <= c):
	print(a)
elif (b <= a) and (b <= c):
	print(b)
else:
	print(c)


# -------------
# Option 2
# -------------
a = 1
b = 2
c = 3

if (a <= b) and (a <= c):
	print(a)
elif (b < a) and (b < c):
	print(b)
else:
	print(c)

# -------------
# Option 3
# -------------
a = 1
b = 3
c = 4

print(max(a, b, c))