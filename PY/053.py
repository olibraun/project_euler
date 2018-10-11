#!/usr/bin/python3

# How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are greater than one-million?

import OBMath

values = []

for n in range(1, 101):
  for k in range(0, n+1):
    values.append( OBMath.binomial(n, k) )

filtered_values = [x for x in values if x > 1000000]    

print(len(filtered_values))