#  Make a program for evaluating this
#  function when m = 0, s = 2, and x = 1. Verify the program’s result by comparing
#  with hand calculations on a calculator.

#from math import pi, exp, sqrt
#m = 0
#s = 2.0
#x = 1.0
#f = 1 / (sqrt(2 * pi) * s) * exp(-0.5 * ((x - m) / s) ** 2)
#print (f)
#0.17603266338214976

import math
m = 0
s = 2.0
x = 1.0
f = 1 / (math.sqrt(2 * math.pi) * s) * math.exp(-0.5*((x - m / s)) ** 2)
print(f)

#0.48394144903828673