#!/usr/bin/python

#The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right,
#and remain prime at each stage: 3797, 797, 97, and 7.
#Similarly we can work from right to left: 3797, 379, 37, and 3.
#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

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
  for x in range(2, rn + 1):
    if n%x == 0:
      return False
  return True

def isLeftTruncatable(n):
  st = str(n)
  l = len(st)
  for i in range(1, l+1):
    sst = st[l-i:l]
    if not isPrime(int(sst)):
      return False
  return True

def isRightTruncatable(n):
  st = str(n)
  l = len(st)
  for i in range(1, l+1):
    sst = st[0:i]
    if not isPrime(int(sst)):
      return False
  return True

truncatable_primes = []
n = 23
while len(truncatable_primes) < 11:
  if isLeftTruncatable(n) and isRightTruncatable(n):
    truncatable_primes.append(n)
  n += 1

print truncatable_primes
print len(truncatable_primes)
print sum(truncatable_primes)