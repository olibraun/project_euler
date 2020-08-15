#!/usr/bin/python

#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#Note: as 1! = 1 and 2! = 2 are not sums they are not included.

def fac(n):
  if n == 0:
    return 1
  else:
    return n*fac(n-1)

factorials_of_digits = [fac(n) for n in range(0, 10)]

#Define faster factorial as a lookup function using the above list factorials_of_digits
def fast_fac(n):
  global factorials_of_digits
  return factorials_of_digits[n]

def digitfac(n):
  sn = str(n)
  return sum([fast_fac(int(c)) for c in sn])

list = []

#Which numbers should be considered?
#10^n <= \sum a_i 10^i = \sum a_i! <= (n+1)*9!

n = 1
while 10**n <= (n+1)*fac(9):
  n += 1

print('The search space is the set of integers up to 10 to the power ' + str(n) + '.')

for n in range(3, 10**n):
  if n == digitfac(n):
    list.append(n)

print('Here are the numbers with the desired property.')
print(list)
print('Their sum is')
print(sum(list))