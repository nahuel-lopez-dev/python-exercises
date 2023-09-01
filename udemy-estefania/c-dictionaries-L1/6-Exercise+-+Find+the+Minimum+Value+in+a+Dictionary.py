my_dict = {"a": 4, "b": 3, "c": 7}

if my_dict:
	min_value = min(set(my_dict.values()))
	print(min_value)
else:
	print(None)