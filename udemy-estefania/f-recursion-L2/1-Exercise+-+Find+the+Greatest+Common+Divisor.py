# ---------------
# Option 1
# ---------------

def find_gcd(a, b):
	if b == 0:
		return a
	else:
		return find_gcd(b, a % b)

# ---------------
# Option 2
# ---------------

import math

a = 4
b = 2

math.gcd(a, b)