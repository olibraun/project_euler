import math

# Die n-stelligen Zahlen liegen zwischen 10**(n-1) und 10**n - 1.
# Die größte n-te Potenz, die wir uns ansehen müssen, ist also 9**n.
# Aus der Ungleichung 10**(n-1) <= 9**n erhalten wir
# n <= (log(9) / log(10/9)) + 1 = 21,85434...
# Also betrachten wir maximal 21-te Potenzen.

def numberOfDigits(n):
  sn = str(n)
  return len(sn)

totalCount = 0

for n in range(1, 21+1):
  count = 0
  for x in range(1, 9 + 1):
    p = x**n
    if numberOfDigits(p) == n:
      count += 1
  totalCount += count
  print(n, count)

print('Total count is', totalCount)
