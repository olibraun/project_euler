#!/usr/bin/python3

# [...]
# However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433*2^7830457+1.
# Find the last ten digits of this prime number.

modulus = 10**10
exponent = 0
power = 1

while exponent < 7830457:
  power *= 2
  power = (power % modulus)
  exponent += 1

prime = (28433 * power + 1) % modulus
print(prime)