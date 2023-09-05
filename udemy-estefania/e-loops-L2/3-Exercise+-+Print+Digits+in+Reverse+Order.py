# ------------
# Option 1
# ------------

num = 352

reverse = int(str(num)[::-1])

print(reverse)

# ------------
# Option 2
# ------------

num = 352
 
reversed_num = 0
 
while num > 0:
  remainder = num % 10
  reversed_num = (reversed_num * 10) + remainder
  num = num // 10
 
print(reversed_num)