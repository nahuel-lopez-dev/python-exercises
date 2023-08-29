# ---------------
# Option 1
# ---------------
my_list = [1, 2, 3, 4]

if len(my_list) > 1:
	sorted_list = sorted(my_list)
	print(sorted_list[1])
else:
	print(None)

# ---------------
# Option 2
# ---------------
my_list = [1, 2, 3, 4]

if len(my_list) > 1:
	no_duplicates = set(my_list)
	no_duplicates.remove(min(no_duplicates))
	print(min(no_duplicates)) 
else:
	print(None)