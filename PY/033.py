#!/usr/bin/python

#The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe
#that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

def iscancellable(num, den):
  if num % 10 == 0 and den % 10 == 0:
    return False
  num_st = str(num)
  den_st = str(den)

  frac_value = float(num)/float(den)

  num_test = float(num_st[0])
  den_test = float(den_st[0])
  num_rem = num_st[1]
  den_rem = den_st[1]
  if num_rem == den_rem:
    if den_test != 0.0 and num_test / den_test == frac_value:
      return True

  num_test = float(num_st[0])
  den_test = float(den_st[1])
  num_rem = num_st[1]
  den_rem = den_st[0]
  if num_rem == den_rem:
    if den_test != 0.0 and num_test / den_test == frac_value:
      return True

  num_test = float(num_st[1])
  den_test = float(den_st[0])
  num_rem = num_st[0]
  den_rem = den_st[1]
  if num_rem == den_rem:
    if den_test != 0.0 and num_test / den_test == frac_value:
      return True

  num_test = float(num_st[1])
  den_test = float(den_st[1])
  num_rem = num_st[0]
  den_rem = den_st[0]
  if num_rem == den_rem:
    if den_test != 0.0 and num_test / den_test == frac_value:
      return True

  return False

#print iscancellable(49, 97)

count = 0
fractions = []
for a in range(10,100):
  for b in range(a + 1,100):
    if iscancellable(a, b):
      fractions.append([a, b])
      count += 1

print count
from sets import Set
print Set([float(x[0])/float(x[1]) for x in fractions])

# This simple four element list contains the fractions 1/4, 1/2, 2/5 and 1/5
# This gives us the answer: (1/4) * (1/2) * (2/5) * (1/5) = (2/200) = 1/100
print 100