#!/usr/bin/python

#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
#For example, 2143 is a 4-digit pandigital and is also prime.
#What is the largest n-digit pandigital prime that exists?

from sets import Set
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

def isPandigital(n):
  sn = str(n)
  nn = len(sn)
  digits = Set([int(x) for x in sn])
  return digits == Set(range(1, nn+1))

#use digit sum and the fact that it is congruent mod 3 to the number in order to exclude some lengths
#for pandigital PRIMES

print 'Start generating search spaces.'
print 'Two digit search space skipped.'
print 'Three digit search space skipped.'
list4 = [n for n in range(1234, 4321+1) if isPandigital(n)]
print 'Four digit search space generated.'
print 'Five digit search space skipped.'
print 'Six digit search space skipped.'
list7 = [n for n in range(1234567, 7654321+1) if isPandigital(n)]
print 'Seven digit search space generated.'
print 'Eight digit search space skipped.'
print 'Nine digit search space skipped.'
print 'All search spaces generated.'

max = 0
for x in list4:
  if isPrime(x):
    max = x

for x in list7:
  if isPrime(x):
    max = x

print max