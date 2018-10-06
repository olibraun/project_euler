#!/usr/bin/python3

mydict = {}

def p(n, m):
  if m == 0:
    return 0
  if n == 0:
    return 1
  if n < 0:
    return 0
  if (n, m-1) not in mydict:
    mydict[(n, m-1)] = p(n, m-1)
  if (n-m, m) not in mydict:
    mydict[(n-m, m)] = p(n-m, m)
  return mydict[(n, m-1)] + mydict[(n-m, m)]

def f(n):
  return p(n, n-1)

# Fill dictionary with potentially useful stuff
for i in range(1, 35):
  for j in range(1, i):
    p(i, j)

res = f(100)
print('There are %d partitions of the requested kind for the number 100.' % res)