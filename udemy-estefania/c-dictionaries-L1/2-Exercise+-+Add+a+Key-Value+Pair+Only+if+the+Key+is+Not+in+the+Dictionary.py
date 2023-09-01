my_dict = {"January": 45, "February": 56, "March": 67}

new_key = "April"
new_value = 67

if new_key not in my_dict:
	my_dict[new_key] = new_value

print(my_dict)