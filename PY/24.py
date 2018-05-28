#!/usr/bin/python

#A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
#If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#012   021   102   120   201   210
#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

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

print l[999999]