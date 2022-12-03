import sys
import math

b, a = map(int, sys.stdin)
theta = math.degrees(math.atan(b / a))
print(f'{round(theta)}\N{DEGREE SIGN}')
