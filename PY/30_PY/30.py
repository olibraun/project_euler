#!/usr/bin/python

#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def sfp(n):
  sn = str(n)
  return sum([int(x)**5 for x in sn])

#Get this from a simple estimation using the decimal representation
n = 1
while (n+1)*(9**5) >= 10**n:
  n += 1

list = []

for x in xrange(2, 10**n):
  if x == sfp(x):
    list.append(x)

print sum(list)