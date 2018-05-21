#!/usr/bin/python

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import math

def isPrime(n):
  if n==1:
    return False
  rn = int(math.ceil(math.sqrt(n)))
  for x in xrange(2, rn):
    if n%x == 0:
      return False
  return True

def smallestPrimeFactor(n):
  for x in xrange(2, n+1):
    if isPrime(x) and n%x == 0:
      return x

def allPrimeFactors(n):
  p = smallestPrimeFactor(n)
  nn = n/p
  if nn == 1:
    return [p]
  else:
    return [p] + allPrimeFactors(nn)

print allPrimeFactors(600851475143)[-1]