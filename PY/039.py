#!/usr/bin/python

#If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#{20,48,52}, {24,45,51}, {30,40,50}
#For which value of p <= 1000, is the number of solutions maximised?

def number_of_solutions(p):
  solutions = 0
  for a in xrange(1, p+1):
    for b in xrange(a, p+1):
      c = p - (a + b)
      if a**2 + b**2 == c**2:
        solutions += 1
  return solutions

maximum = 1
maximizer = 1

for p in xrange(1, 1000 + 1):
  n = number_of_solutions(p)
  if n > maximum:
    maximum = n
    maximizer = p

print maximizer