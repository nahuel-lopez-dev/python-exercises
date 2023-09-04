# ---------------
# Option 1
# ---------------
year = 1836

if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			print(f"{year} is a leap year")
		else:
			print(f"{year} is not a leap year")
	else:
		print(f"{year} is a leap year") 
else:
	print(f"{year} is not a leap year")

# ---------------
# Option 2
# ---------------
year = 1836

if year % 400 == 0:
	print(f"{year} is a leap year")
elif year % 100 == 0:
	print(f"{year} is not a leap year")
elif year % 4 == 0:
	print(f"{year} is a leap year")
else:
	print(f"{year} is not a leap year")

# ---------------
# Option 3
# ---------------
year = 1836

if year % 4 != 0:
	print(f"{year} is not a leap year")
elif year % 100 != 0:
	print(f"{year} is a leap year")
elif year % 400 != 0:
	print(f"{year} is not a leap year")
else:
	print(f"{year} is a leap year")
