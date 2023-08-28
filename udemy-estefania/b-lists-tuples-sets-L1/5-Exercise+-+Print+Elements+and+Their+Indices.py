# ===============
# Option 1
# ===============

my_list = [1, 2, 3, 4]

if len(my_list) == 0:
	print("Empty List")
else:
	for i in range(len(my_list)):
		print(my_list[i], i)

# ===============
# Option 2
# ===============

my_list = [1, 2, 3, 4]

if not my_list:
	print("Empty List")
else:
	for i, elem in enumerate(my_list):
		print(elem, i)
