#!/usr/bin/python

#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
#for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

from sets import Set

alldigits = Set([str(x) for x in range(1, 10)])

panprods = []

for a in range(1, 9876 + 1):
  blimit = int( (9876/a) + 1 )
  for b in range(a, blimit):
    p = a*b
    digits = Set([x for x in str(a)] + [x for x in str(b)] + [x for x in str(p)])
    if digits == alldigits:
      panprods.append(p)

print sum(Set(panprods))