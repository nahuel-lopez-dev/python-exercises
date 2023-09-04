import math

a = 2
b = 5 
c = -3

discriminant = b**2 - 4*a*c

if discriminant < 0:
	print("Complex Roots")
elif discriminant == 0:
	r = (-b + math.sqrt(discriminant))/(2*a)
	print(r)
else:
	r1 = (-b - math.sqrt(discriminant))/(2*a)
	r2 = (-b + math.sqrt(discriminant))/(2*a)
	print(r1, r2)