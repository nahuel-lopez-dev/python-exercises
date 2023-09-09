import datetime

date1_input = input("Enter the first date: ")
date2_input = input("Enter the second date: ")

date1_list = date1_input.split(" ")
year1 = int(date1_list[0])
month1 = int(date1_list[1])
day1 = int(date1_list[2])

date1_obj = datetime.date(year1, month1, day1)

date2_list = date2_input.split(" ")
year2 = int(date2_list[0])
month2 = int(date2_list[1])
day2 = int(date2_list[2])

date2_obj = datetime.date(year2, month2, day2)

if date2_obj < date1_obj:
    print("Please enter valid dates.")
else:
    difference = (date2_obj - date1_obj).days

    if difference == 0:
        print("These dates are equal.")
    elif difference == 1:
    	print(f"There is 1 day between these dates.")
    else:
        print(f"There are {difference} days between these dates.")