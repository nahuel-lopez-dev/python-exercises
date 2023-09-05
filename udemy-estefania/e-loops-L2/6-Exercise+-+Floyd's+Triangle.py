# -----------
# Option 1
# -----------

n = int(input("Enter the number of rows: "))

count = 1

for i in range(1, n+1):
    for j in range(0, i):
        print(count, end=" ")
        count += 1
    print()

# -----------
# Option 2: Default Value of Start
# -----------

n = int(input("Enter the number of rows: "))

count = 1

for i in range(1, n+1):
    for j in range(i):
        print(count, end=" ")
        count += 1
    print()

