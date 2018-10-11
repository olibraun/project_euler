#!/usr/bin/python

#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen)
#contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

import math

def lettercount(n):
  # Special cases 1 through 19
  if n == 1 or n ==2 or n == 6 or n == 10:
    return 3
  elif n == 3 or n == 7 or n == 8:
    return 5
  elif n == 4 or n == 5 or n == 9:
    return 4
  elif n == 11 or n == 12:
    return 6
  elif n == 13 or n == 14 or n == 18 or n == 19:
    return 8
  elif n == 15 or n == 16:
    return 7
  elif n == 17:
    return 9

  # Multiples of ten
  if n == 20 or n == 30 or n == 80 or n == 90:
    return 6
  elif n == 40 or n == 50 or n == 60:
    return 5
  elif n == 70:
    return 7

  # Multiples of 100:
  if 100 <= n <= 900 and n % 100 == 0:
    firstdigit = math.floor(n/100)
    return lettercount(firstdigit) + 7

  # "Composites"
  if 20 <= n <= 99:
    lastdigit = n % 10
    firstdigit = math.floor(n/10)
    return lettercount(10*firstdigit) + lettercount(lastdigit)

  if 100 <= n <= 999:
    lasttwo = n % 100
    firstdigit = math.floor(n/100)
    return lettercount(100*firstdigit) + len('and') + lettercount(lasttwo)

  if n == 1000:
    #one thousand
    return 3 + 8

print sum([lettercount(n) for n in xrange(1, 1000 + 1)])