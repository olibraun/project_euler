#!/usr/bin/python

#The first two consecutive numbers to have two distinct prime factors are:
#14 = 2 * 7
#15 = 3 * 5
#The first three consecutive numbers to have three distinct prime factors are:
#644 = 2^2 * 7 * 23
#645 = 3 * 5 * 43
#646 = 2 * 17 * 19.
#Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

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
  for x in xrange(2, rn + 1):
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

factors = {1: []}
number_of_factors = {1: 0}

def get_number_of_factors(n):
  global number_of_factors
  if n in number_of_factors:
    return number_of_factors[n]
  else:
    p = smallestPrimeFactor(n)
    np = n/p
    fnp = list(factors[np])
    fnp.append(p)
    factors[n] = fnp
    nn = len(Set(fnp))
    number_of_factors[n] = nn
    return nn

found = False

print 'This program will run for about 20 minutes. It will find the correct answer, which is 134043.'

n = 2
while not found:
  if n % 15000 == 0:
    print 'I\'m at ' + str(n) + '.'
    #print number_of_factors
  f0 = get_number_of_factors(n+0)
  f1 = get_number_of_factors(n+1)
  f2 = get_number_of_factors(n+2)
  f3 = get_number_of_factors(n+3)
  if 4 == f0 == f1 == f2 == f3:
    found = True
    print n
  n += 1