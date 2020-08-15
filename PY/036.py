#!/usr/bin/python

#The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.
#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#(Please note that the palindromic number, in either base, may not include leading zeros.)

import math

def isPalindrome(n):
  nn = str(n)
  return nn == nn[::-1]

def convertToBaseTwo(n):
  res = ''
  e2 = int(math.floor( math.log10(n) / math.log10(2) ))
  for e in range(e2, -1, -1):
    p = 2**e
    if n & p == p:
      res += '1'
    else:
      res += '0'
  return int(res)

def is_10_2_palindrome(n):
  return isPalindrome(n) and isPalindrome(convertToBaseTwo(n))

print(sum([n for n in range(1,1000000) if is_10_2_palindrome(n)]))