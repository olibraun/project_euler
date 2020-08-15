#!/usr/bin/python

#Interestingly, phi(87109)=79180, and it can be seen that 87109 is a permutation of 79180.
#Find the value of n, 1 < n < 10^7, for which phi(n) is a permutation of n and the ratio n/phi(n) produces a minimum.

import math
from sets import Set

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

def smallestPrimeFactor(n):
  for x in range(2, n+1):
    if isPrime(x) and n%x == 0:
      return x

def gcd(x, y):
  while y != 0:
    (x, y) = (y, x % y)
  return x

def completeSmallestPrimeFactor(n):
  p = smallestPrimeFactor(n)
  exp = 0
  while gcd(p,n) != 1:
    exp += 1
    n = (n/p)
  return [p,exp]

def completePrimeFactorization(n):
  factors = []
  while n != 1:
    f = completeSmallestPrimeFactor(n)
    factors.append(f)
    n = (n / f[0]**f[1])
  return factors

def phi(n):
  if n == 1:
    return 1
  res = 1
  for f in completePrimeFactorization(n):
    res *= ( (f[0]**(f[1]-1)) * (f[0]-1) )
  return res

def phi2(p1,p2):
  return (p1-1)*(p2-1)

def getProperty(n):
  sn = str(n)
  pn = phi(n)
  spn = str(pn)
  if Set([x for x in sn]) == Set([x for x in spn]):
    return float(n)/float(pn)
  else:
    return 10**10

def getProperty2(p1,p2):
  n = p1*p2
  sn = str(n)
  pn = phi2(p1,p2)
  spn = str(pn)
  if Set([x for x in sn]) == Set([x for x in spn]):
    return float(n)/float(pn)
  else:
    return 10**10

candidates = [x for x in range(2, 10**7 / 2) if x % 3 == 1 or x % 3 == 2]
candidates2 = [x for x in candidates if isPrime(x)]

print 'Search space set up.'

minimum = 10**10
bestn = 0
l = len(candidates2)
limit = 10**7
for i in range(l):
  j = i
  p1 = candidates2[i]
  p2 = candidates2[j]
  n = p1*p2
  print 'Checking for p1=' + str(p1) + '.'
  while n < limit:
    print '  Checking for p2=' + str(p2) + '.'
    p = getProperty2(p1,p2)
    if p < minimum:
      minimum = p
      bestn = n
    if j+1 < l:
      j += 1
    else:
      n = limit + 1
    p2 = candidates2[j]
    n = p1*p2

print bestn