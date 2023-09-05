# ----------
# Option 1
# ----------

n = int(input("Enter the number of rows: "))

k = (2 * n) - 2

for i in range(0, n):

    for j in range(0, k):
        print("", end=" ")

    k = k - 2

    for j in range(0, i + 1):
        print("*", end=" ")

    print("")

# ----------
# Option 2: Using Default Start Values
# ----------

n = int(input("Enter the number of rows: "))

k = (2 * n) - 2

for i in range(n):

    for j in range(k):
        print("", end=" ")

    for j in range(i + 1):
        print("*", end=" ")

    print("")

    k = k - 2