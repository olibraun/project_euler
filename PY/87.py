#!/usr/bin/python3

#How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?

import OBMath

limit = 50000000
slimit = int(limit**(1/2))
climit = int(limit**(1/3))
qlimit = int(limit**(1/4))

sprimes = [x for x in range(1, slimit) if OBMath.isPrime(x)]
cprimes = [x for x in range(1, climit) if OBMath.isPrime(x)]
qprimes = [x for x in range(1, qlimit) if OBMath.isPrime(x)]

numbers = set(())
for p in sprimes:
  for q in cprimes:
    for r in qprimes:
      number = p**2 + q**3 + r**4
      if number < limit:
        numbers.add(number)

print(len(numbers))