#!/usr/bin/python

#We can easily verify that none of the entries in the first seven rows of Pascal's triangle are divisible by 7:
#  	  	  	  	  	  	 1
#  	  	  	  	  	 1 	  	 1
#  	  	  	  	 1 	  	 2 	  	 1
#  	  	  	 1 	  	 3 	  	 3 	  	 1
#  	  	 1 	  	 4 	  	 6 	  	 4 	  	 1
#  	 1 	  	 5 	  	10 	  	10 	  	 5 	  	 1
#1 	  	 6 	  	15 	  	20 	  	15 	  	 6 	  	 1
#However, if we check the first one hundred rows, we will find that only 2361 of the 5050 entries are not divisible by 7.
#Find the number of entries which are not divisible by 7 in the first one billion (10^9) rows of Pascal's triangle.

#IDEA: Use https://en.wikipedia.org/wiki/Kummer's_theorem

import math

# powerlist = [7**k for k in range(0, 10**9/2 + 1)]
# print 'List of powers created.'

def convertToBase(x, b):
  """
  Converts given number x, from base 10 to base b
  x -- the number in base 10
  b -- base to convert
  """
  assert(x >= 0)
  assert(1< b < 37)
  r = ''
  import string
  while x > 0:
    r = string.printable[x % b] + r
    x //= b
  # return the result string as a list in reverse order
  rr = [x for x in r]
  rr.reverse()
  return rr

def countCarries7(a, b):
  count = 0
  res = [0]
  ma = max(len(a), len(b))
  if len(a) > len(b):
    for i in range(min(len(a), len(b)), ma):
      b.append(0)
  else:
    for i in range(min(len(a), len(b)), ma):
      a.append(0)

  for i in range(0, ma):
    temp = res[i] + int(a[i]) + int(b[i])
    carry = 0
    while temp >= 7:
      carry += 1
      count += 1
      temp -= 7
    res[i] = temp
    res.append(carry)
  if res[-1] == 0:
    res = res[:-1]
  return count

# a = convertToBase(8, 7)
# b = convertToBase(6, 7)
# print a
# print b
# print countCarries7(a, b)

def v7(n):
  maxexp = 0
  while 7**maxexp <= n:
    maxexp += 1
  return sum([math.floor(n/7**k) for k in range(1, maxexp + 1)])

def checkproperty(n, k):
  return v7(n) - v7(k) - v7(n - k) == 0

def checkproperty2(n, k):
  n7 = convertToBase(k, 7)
  k7 = convertToBase(n-k, 7)
  return countCarries7(n7, k7) == 0

rows = 10**9
count = 1

for n in range(1, rows):
  if n%10000 == 0:
    print 'n=' + str(n)
  klimit = int(math.ceil(n / 2))
  count += 2 #for the outer entries
  for k in range(1, klimit + 1):
    if checkproperty2(n, k):
      if n % 2 == 0 and k == klimit:
        count += 1
      else:
        count += 2

print count