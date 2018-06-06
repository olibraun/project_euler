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

limit = 1000000
primes = [x for x in xrange(1, limit) if isPrime(x)]

print 'List of primes generated, beginning the search.'

longest_sequence = []
for i in xrange(0, len(primes) - 1):
  value = 0
  j = i
  sequence = []
  while value < limit:
    p = primes[j]
    value += p
    if value < limit:
      sequence.append(p)
      if isPrime(value) and len(sequence) > len(longest_sequence):
        longest_sequence = list(sequence)
    if j + 1 < len(primes):
      j += 1
  if i % 20000 == 0 and i != 0:
    print 'First ' + str(i) + ' primes checked.'

message = 'The result is ' + str(sum(longest_sequence)) 
message += ', which is the sum of ' + str(len(longest_sequence))
message += ' consecutive primes starting with ' + str(min(longest_sequence)) + '.'

print message
