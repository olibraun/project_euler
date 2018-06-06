#!/usr/bin/python

#It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

from sets import Set

def digits(n):
  sn = [x for x in str(n)]
  return Set(sn)


def checkProperty(n):
  dn = digits(n)
  d2n = digits(2*n)
  if dn != d2n:
    return False
  d3n = digits(3*n)
  if dn != d3n:
    return False
  d4n = digits(4*n)
  if dn != d4n:
    return False
  d5n = digits(5*n)
  if dn != d5n:
    return False
  d6n = digits(6*n)
  if dn != d6n:
    return False
  return True

done = False
n = 0
while not done:
  n += 1
  if checkProperty(n):
    done = True
print n
