# -----------------
# Option 1
# -----------------

pointA = [3, 4, 5]
pointB = [1, 3, 5]

distance = ((pointA[0] - pointB[0])**2
			+ (pointA[1] - pointB[1])**2
			+ (pointA[2] - pointB[2])**2)**(1/2)

print(distance)

# -----------------
# Option 2
# -----------------

import math

pointA = [3, 4, 5]
pointB = [1, 3, 5]

addition = ((pointA[0] - pointB[0])**2
			+ (pointA[1] - pointB[1])**2
			+ (pointA[2] - pointB[2])**2)

distance = math.sqrt(addition)

print(distance)
