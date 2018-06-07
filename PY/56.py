#!/usr/bin/python

#A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large:
#one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
#Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

from sets import Set

def digitsum(n):
  nn = str(n)
  return sum([int(x) for x in nn])

powers = []
for a in xrange(1, 100):
  for b in xrange(1, 100):
    powers.append(a**b)

powers = Set(powers)

print max([digitsum(x) for x in powers])