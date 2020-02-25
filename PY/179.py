import math

limit = 10**7

divisors = [0]*(limit + 1)

for i in range(1, math.floor(limit/2)+1):   # Loop over all numbers which can be divisors
  for j in range(i, limit, i):              # and over all of their multiples
    divisors[j] += 1

count = 0
for i in range(1, limit):
  if divisors[i] == divisors[i+1]:
    count += 1

print(count)
