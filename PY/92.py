#!/usr/bin/python

#A number chain is created by continuously adding the square of the digits in a number 
#to form a new number until it has been seen before.

#For example,
#44 -> 32 -> 13 -> 10 -> 1 -> 1
#85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
#Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. 
#What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
#How many starting numbers below ten million will arrive at 89?

def step(n):
  sn = str(n)
  return sum([int(x)**2 for x in sn])

endValues = {}
endValues[1] = 1
endValues[89] = 89

def endValue(n):
  global endValues
  x = n
  if x in endValues:
    return endValues[x]
  memory = [n]
  while True:
    x = step(x)
    if x not in endValues:
      memory.append(x)
    else:
      ev = endValues[x]
      for i in memory:
        endValues[i] = ev
      return ev

L = [x for x in xrange(1, 10000000) if endValue(x) == 89]
print len(L)
