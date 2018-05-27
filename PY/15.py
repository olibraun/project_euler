#!/usr/bin/python

#Starting in the top left corner of a 2*2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20*20 grid?

#This will have 40 steps from start to finish.
#Each step will either be "right" or "down" and there will be 20 of each kind.
#How are the "right"'s positioned? That determines the other positions.

def fac(n):
  if n == 0:
    return 1
  return n * fac(n - 1)

print fac(40)/(fac(20)*fac(20))