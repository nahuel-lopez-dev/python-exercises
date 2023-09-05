height = int(input("Enter the diamond's height (an odd number): "))

if height % 2 == 0:
    print("Please enter an odd value for the height (number of rows).")
else:
    middle_rows = (height + 2) // 2

    for i in range(middle_rows):
        print(" " * (middle_rows - i), "*" * (i*2 + 1))

    for i in range(middle_rows-2, -1, -1):
        print(" " * (middle_rows - i), "*" * (i*2 + 1))
