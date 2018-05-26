#!/usr/bin/python

import math

def isTriagonal(n):
  totest = (math.sqrt(8*n+1)-1)/2
  return totest.is_integer()

def isPentagonal(x):
  totest = (math.sqrt(24*x+1) + 1)/6
  return totest.is_integer()

def H(n):
  return n*(2*n-1)

n = 144
done = False

while not done:
  h = H(n)
  if isPentagonal(h) and isTriagonal(h):
    print h
    done = True
  n += 1