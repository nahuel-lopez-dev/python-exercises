# ================
# Option 1
# ================

my_list = [3, 4, 5, 6]
factor = 2

for i in range(len(my_list)):
	my_list[i] *= factor

print(my_list)

# ================
# Option 2
# ================

my_list = [3, 4, 5, 6]
factor = 2

for i, elem in enumerate(my_list):
	my_list[i] = elem * factor

print(my_list)

