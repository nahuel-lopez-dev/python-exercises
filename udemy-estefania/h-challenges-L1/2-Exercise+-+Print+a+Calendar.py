import calendar

print("Welcome to your Python Calendar")
year = int(input("Enter the year (with this format YYYY): "))
month = int(input("Now enter the month (1-12): "))

print(calendar.month(year, month))