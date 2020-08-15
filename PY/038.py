#!/usr/bin/python

#Take the number 192 and multiply it by each of 1, 2, and 3:
#    192 * 1 = 192
#    192 * 2 = 384
#    192 * 3 = 576
#By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
#which is the concatenated product of 9 and (1,2,3,4,5).
#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with
#(1,2, ... , n) where n > 1?

from sets import Set
import math

def concatenatedProduct(n, l):
  res = ''
  for f in l:
    res += str(n*f)
  return int(res)

def is19Pandigital(n):
  if n < 123456789:
    return False
  digits = [int(x) for x in str(n)]
  digitsSet = Set(digits)
  return len(digits) == 9 and digitsSet == Set([1,2,3,4,5,6,7,8,9])

def noDoubleDigits(n):
  st = str(n)
  return len(Set([x for x in st])) == len(st)

currentlargest = 0
currenti = 0
currentn = 0
for n in range(2, 10):
  for i in range(1, 9999):
    #i may not contain double digits
    if noDoubleDigits(i):
      concat = concatenatedProduct(i, range(1,n))
      if is19Pandigital(concat) and concat > currentlargest:
        currentlargest = concat
        currenti = i
        currentn = n

print currentlargest
print 'Obtained as the concatenated product of ' + str(currenti) + ' and the interval 1,...,' + str(currentn-1) + '.'
print concatenatedProduct(9327,[1,2])