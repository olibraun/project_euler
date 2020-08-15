#!/usr/bin/python

#Consider quadratic Diophantine equations of the form:
#x^2 - Dy^2 = 1
#For example, when D=13, the minimal solution in x is 6492 - 13*1802 = 1.
#It can be assumed that there are no solutions in positive integers when D is square.
#By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
#3^2 - 2*2^2 = 1
#2^2 - 3*1^2 = 1
#9^2 - 5*4^2 = 1
#5^2 - 6*2^2 = 1
#8^2 - 7*3^2 = 1
#Hence, by considering minimal solutions in x for D <= 7, the largest x is obtained when D=5.
#Find the value of D <= 1000 in minimal solutions of x for which the largest value of x is obtained.

import math

maxD = 1000
D = 2
current_best_D = 0
current_max_x = 0

while D <= maxD:
  if D%50 == 0:
    print '50 done.'
  if not (math.sqrt(D)).is_integer():
    x = 1
    solution = False
    while not solution:
      x2 = x**2
      if x2 % D == 1:
        for y in range(1, x + 1):
          if x2 - D*y**2 == 1:
            solution = True
            if x >= current_max_x:
              current_max_x = x
              current_best_D = D
            break
      if D%2 == 0:
        x+=2
      else:
        x+=1
  D += 1

print current_best_D