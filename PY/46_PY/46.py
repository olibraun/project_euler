#!/usr/bin/python

#It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#9 = 7 + 2*1^2
#15 = 7 + 2*2^2
#21 = 3 + 2*3^2
#25 = 7 + 2*3^2
#27 = 19 + 2*2^2
#33 = 31 + 2*1^2
#It turns out that the conjecture was false.
#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

import math

def isPrime(n):
  if n < 0:
    n *= -1
  if n == 0:
    return False
  if n == 1:
    return False
  if n == 2:
    return True
  rn = int(math.ceil(math.sqrt(n)))
  for x in xrange(2, rn + 1):
    if n%x == 0:
      return False
  return True

limit = 100000
rlimit = int(math.ceil(math.sqrt(limit)))
primes = [p for p in xrange(2, limit) if isPrime(p)]
odd_composites = [n for n in xrange(9, limit) if n%2 == 1 and not isPrime(n)]
squares = [n**2 for n in xrange(1, rlimit)]

def isGoldbach(n):
  global primes
  global squares
  has_property = False
  for p in primes:
    if p > n:
      break
    totest = (n-p)/2.0
    if totest.is_integer():
      totest = int(totest)
      for s in squares:
        if s > totest:
          break
        if totest == s:
          has_property = True
          break
  return has_property

for n in odd_composites:
  if not isGoldbach(n):
    print n
    break