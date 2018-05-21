#!/usr/bin/python

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10001st prime number?

import math

def isPrime(n):
  if n==1:
    return False
  if n==2:
    return True
  rn = int(math.ceil(math.sqrt(n)))
  for x in xrange(2, rn + 1):
    if n%x == 0:
      return False
  return True

primes = [2]
current = 3
while len(primes) < 10001:
  if isPrime(current):
    primes.append(current)
  current += 1

print primes[-1]