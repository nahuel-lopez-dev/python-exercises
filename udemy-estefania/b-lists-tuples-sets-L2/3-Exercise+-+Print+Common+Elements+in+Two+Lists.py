listA = [1, 2, 3, 4]
listB = [1, 2, 3, 4]

common_elem = []

for elem in listA:
	if elem in listB:
		common_elem.append(elem)

print(common_elem)