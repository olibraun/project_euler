#!/usr/bin/python

#The series 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#Find the last ten digits of the series 1^1 + 2^2 + 3^3 + ... + 1000^1000.

res = 0
modulus = 10**10
for n in range(1, 1001):
  res += ( ((n % modulus)**n) % modulus  )

print res % modulus