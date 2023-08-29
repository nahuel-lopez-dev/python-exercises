listA = [1, 2, 3, 4]
listB = [1, 2]

difference = []

for elem in listA:
	if elem not in listB:
		difference.append(elem)

print(difference)
