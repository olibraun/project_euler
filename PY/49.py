#!/usr/bin/python

#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
#(i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
#but there is one other 4-digit increasing sequence.
#What 12-digit number do you form by concatenating the three terms in this sequence?

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

#Look at sequences of the form, n, n+q, n+2q where n starts at 1009 (smallest four digit prime)
#and q <= (9973-n)/2, 9973 being the largest four digit prime.
#n needs to go up to the third to last four digit prime, which is 9949

def checkSequence(l):
  if len(l) != 3:
    return False
  a = l[0]
  b = l[1]
  c = l[2]
  
  if not (isPrime(a) and isPrime(b) and isPrime(c)):
    return False

  #Are the numbers permutations of each other?
  sa = Set([x for x in str(a)])
  sb = Set([x for x in str(b)])
  sc = Set([x for x in str(c)])
  if not sa == sb == sc:
    return False

  return True

n = 1009
solution = []
while n <= 9949:
  qlimit = int(math.ceil((9973-n)/2))
  for q in xrange(1, qlimit + 1):
    seq = [n, n+q, n + 2*q]
    if checkSequence(seq) and not (n == 1487 and q == 3330):
      solution = seq
  n += 2

print str(solution[0]) + str(solution[1]) + str(solution[2])