#!/usr/bin/python

#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#How many circular primes are there below one million?

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

def checkRotations(n):
  st = str(n)
  st1 = st
  l = len(st)

  if not isPrime(int(st1)):
    return False

  count = 0
  while count < l - 1:
    st1 = st1[-1] + st1[0:l-1]
    if not isPrime(int(st1)):
      return False
    count += 1

  return True

counter = 0
for i in range(2, 1000000):
  if checkRotations(i):
    counter += 1

print counter