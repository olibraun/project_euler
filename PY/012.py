#!/usr/bin/python

#The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#Let us list the factors of the first seven triangle numbers:
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
#We can see that 28 is the first triangle number to have over five divisors.
#What is the value of the first triangle number to have over five hundred divisors?

import math

def isPrime(n):
  if n==1:
    return False
  if n==2:
    return True
  rn = int(math.ceil(math.sqrt(n)))
  for x in range(2, rn + 1):
    if n%x == 0:
      return False
  return True

def triangle(n):
  return n*(n+1)/2

def number_of_divisors(n):
  rn = int(math.ceil(math.sqrt(n)))
  return 2*len([x for x in range(1, rn+1) if n%x == 0])

found = False
n = 1
while not found:
  t = triangle(n)
  ndiv = number_of_divisors(t)
  if ndiv > 500:
    print t
    found = True
  else:
    n += 1