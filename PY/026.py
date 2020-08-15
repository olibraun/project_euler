#!/usr/bin/python

#A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#    1/2	= 	0.5
#    1/3	= 	0.(3)
#    1/4	= 	0.25
#    1/5	= 	0.2
#    1/6	= 	0.1(6)
#    1/7	= 	0.(142857)
#    1/8	= 	0.125
#    1/9	= 	0.(1)
#    1/10	= 	0.1
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

#There are formulas for this. They are based on a factorization of the denominator into a factor coprime to ten (or another base) and
#a complementary factor.

import math

def fact(d):
  e2 = 0
  while d % 2**e2 == 0:
    e2 += 1
  e2 -= 1
  e5 = 0
  while d % 5**e5 == 0:
    e5 += 1
  e5 -= 1
  d1 = 2**e2 * 5**e5
  d2 = d/d1
  return [d1, d2]

def period_length(d):
  f = fact(d)
  p = 1
  while (10**p - 1) % f[1] != 0:
    p += 1
  return p

d_record = 1
d_record_holder = 1
for d in range(2, 1000):
  l = period_length(d)
  if l > d_record:
    d_record = l
    d_record_holder = d

print d_record_holder