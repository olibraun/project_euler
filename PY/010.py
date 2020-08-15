#!/usr/bin/python

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

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

print sum([x for x in range(1, 2000000) if isPrime(x)])