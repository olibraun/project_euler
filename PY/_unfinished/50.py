#!/usr/bin/python

#The prime 41, can be written as the sum of six consecutive primes:
#41 = 2 + 3 + 5 + 7 + 11 + 13
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#Which prime, below one-million, can be written as the sum of the most consecutive primes?

import math

def isPrime(n):
  if n < 0:
    n *= -1
  if n == 0:
    return False
  if n == 1:
    return False
  if n == 2:
    return True
  rn = int(math.ceil(math.sqrt(n)))
  for x in xrange(2, rn + 1):
    if n%x == 0:
      return False
  return True

limit = 100
primes = [x for x in xrange(1, limit) if isPrime(x)]

longest_sequence = []

for i in xrange(0, len(primes)):
  current_sequence = []
  current_sequence.append(primes[i])
  n = i+1
  while isPrime(sum(current_sequence)) and n < len(primes):
    current_sequence.append(primes[n])
    n += 1
  if len(current_sequence) > len(longest_sequence):
    longest_sequence = current_sequence

print longest_sequence
print sum(longest_sequence)