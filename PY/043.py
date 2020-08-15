#!/usr/bin/python

#The number 1406357289 is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
#but it also has a rather interesting sub-string divisibility property.
#Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#    d2d3d4=406 is divisible by 2
#    d3d4d5=063 is divisible by 3
#    d4d5d6=635 is divisible by 5
#    d5d6d7=357 is divisible by 7
#    d6d7d8=572 is divisible by 11
#    d7d8d9=728 is divisible by 13
#    d8d9d10=289 is divisible by 17
#Find the sum of all 0 to 9 pandigital numbers with this property.

from sets import Set

def hasProperty(n):
  st = str(n)
  d = [x for x in st]

  if len(d) != 10 or Set(d) != Set([str(n) for n in range(0, 10)]):
    return False

  if int(d[1] + d[2] + d[3]) % 2 != 0:
    return False

  if int(d[2] + d[3] + d[4]) % 3 != 0:
    return False

  if int(d[3] + d[4] + d[5]) % 5 != 0:
    return False

  if int(d[4] + d[5] + d[6]) % 7 != 0:
    return False

  if int(d[5] + d[6] + d[7]) % 11 != 0:
    return False

  if int(d[6] + d[7] + d[8]) % 13 != 0:
    return False

  if int(d[7] + d[8] + d[9]) % 17 != 0:
    return False

  return True

# n = 1234567890
# res = 0
# while n <= 9876543210:
#   if hasProperty(n):
#     res += n
#   n += 1

# print res


l = []
s = '0123456789'

for a in s:
  s0 = s.replace(a, '')
  for b in s0:
    s1 = s0.replace(b, '')
    for c in s1:
      s2 = s1.replace(c, '')
      for d in s2:
        s3 = s2.replace(d, '')
        for e in s3:
          s4 = s3.replace(e, '')
          for f in s4:
            s5 = s4.replace(f, '')
            for g in s5:
              s6 = s5.replace(g, '')
              for h in s6:
                s7 = s6.replace(h, '')
                for i in s7:
                  s8 = s7.replace(i, '')
                  for j in s8:
                    l.append(a+b+c+d+e+f+g+h+i+j)

ll = [int(x) for x in l]
print sum([n for n in ll if hasProperty(n)])