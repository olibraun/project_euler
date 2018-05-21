#!/usr/bin/python

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which
#a^2 + b^2 = c^2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

for a in xrange(1, 1000):
  for b in xrange(a, 1000):
    for c in xrange(b, 1000 - a - b + 1):
      if a**2 + b**2 == c**2:
        if a + b + c == 1000:
          print a*b*c