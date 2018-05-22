#!/usr/bin/python

#The Fibonacci sequence is defined by the recurrence relation:
#Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
#Hence the first 12 terms will be:
#[...]
#The 12th term, F12, is the first term to contain three digits.
#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

import math

def number_of_digits(n):
  return int(math.floor(math.log10(n)) + 1)

fib = [1, 1]

done = False

while not done:
  current = fib[-1] + fib[-2]
  fib.append(current)
  if number_of_digits(current) >= 1000:
    done = True

print len(fib)