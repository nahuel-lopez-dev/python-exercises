my_dict = {"a": 4, "b": 3, "c": 7}

if my_dict:
	max_value = max(set(my_dict.values()))
	print(max_value)
else:
	print(None)