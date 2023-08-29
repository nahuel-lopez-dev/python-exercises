# ---------------
# Option 1
# ---------------
my_list = [1, 2, 3, 4]

if len(my_list) > 1:
	sorted_list = sorted(my_list)
	print(sorted_list[-2])
else:
	print(None)

# ---------------
# Option 2
# ---------------
my_list = [1, 2, 3, 4]

if len(my_list) > 1:
	no_duplicates = set(my_list)
	no_duplicates.remove(max(no_duplicates))
	print(max(no_duplicates)) 
else:
	print(None)


	