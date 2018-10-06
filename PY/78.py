#!/usr/bin/python3

import OBMath
import sys

sys.setrecursionlimit(8000)

def p(n):
  return OBMath.Partitions.fast_p(n)

# Find the least value of n for which p(n) is divisible by one million.

P2 = 2**6
P5 = 5**6

def isDivisible(n):
  if(n % 2 != 0 or n % 5 != 0):
    return False
  if(n % P2 != 0):
    return False
  if(n % P5 != 0):
    return False
  return True

done = False
i = 1

print("Searching...")

while not done:
  done = isDivisible(p(i))
  i += 1

print(i-1)