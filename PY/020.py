#!/usr/bin/python

#Find the sum of the digits in the number 100!

def digitsum(n):
  nn = str(n)
  return sum([int(x) for x in nn])

def fac(n):
  if n == 0:
    return 1
  else:
    return n*fac(n-1)

print(digitsum(fac(100)))