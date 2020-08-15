#!/usr/bin/python

#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2^1000?

def digitsum(n):
  nn = str(n)
  return sum([int(x) for x in nn])

print(digitsum(2**1000))