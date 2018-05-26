#!/usr/bin/python

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(n):
  nn = str(n)
  return nn == nn[::-1]

pals = []

for a in xrange(100, 1000):
  for b in xrange(a, 1000):
    p = a*b
    if isPalindrome(p):
      pals.append(p)

print max(pals)