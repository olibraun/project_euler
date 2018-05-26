#!/usr/bin/python

#An irrational decimal fraction is created by concatenating the positive integers:
#0.123456789101112131415161718192021...
#It can be seen that the 12th digit of the fractional part is 1.
#If dn represents the nth digit of the fractional part, find the value of the following expression.
#d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000

champ = '0'
n = 1

while len(champ) <= 1000000:
  champ += str(n)
  n += 1

result = int(champ[1])
result *= int(champ[10])
result *= int(champ[100])
result *= int(champ[1000])
result *= int(champ[10000])
result *= int(champ[100000])
result *= int(champ[1000000])

print result