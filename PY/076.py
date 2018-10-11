#!/usr/bin/python3

import OBMath

# Alternative to import everything into the current "main namespace"
# from OBMath import *

def f(n):
  return OBMath.Partitions.p(n, n-1)

res = f(100)
print('There are %d partitions of the requested kind for the number 100.' % res)