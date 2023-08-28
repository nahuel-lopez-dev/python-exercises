# ==================
# Option 1
# ==================

my_list = [1, 1, 2, 3, 4, 4]
no_duplicates = list(set(my_list))
print(no_duplicates)

# ==================
# Option 2
# ==================

my_list = [1, 1, 2, 3, 4, 4]
no_duplicates = list(dict.fromkeys(my_list))
print(no_duplicates)


