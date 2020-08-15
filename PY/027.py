#!/usr/bin/python

#Euler discovered the remarkable quadratic formula:
#n^2+n+41
#It turns out that the formula will produce 40 primes for the consecutive integer values 0<=n<=39.
#However, when n=40,40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,41^2+41+41
#is clearly divisible by 41.
#The incredible formula n^2-79n+1601
#was discovered, which produces 80 primes for the consecutive values 0<=n<=79.
#The product of the coefficients, -79 and 1601, is -126479.
#Considering quadratics of the form:
#n^2+an+b,
#where |a|<1000 and |b|<=1000, where |n| is the modulus/absolute value of n, e.g. |11|=11 and |-4|=4
#Find the product of the coefficients, a and b,
#for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

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
  for x in range(2, rn + 1):
    if n%x == 0:
      return False
  return True

def number_of_primes(a, b):
  def f(x):
    return x**2 + a*x +b

  n = 0
  count = 0
  ok = True
  while ok:
    val = f(n)
    if isPrime(val):
      count += 1
      n += 1
    else:
      ok = False

  return count

max = 0
record_holder_a = 0
record_holder_b = 0
for a in range(-999, 1000):
  for b in range(-1000, 1001):
    num = number_of_primes(a, b)
    if num > max:
      max = num
      record_holder_a = a
      record_holder_b = b

print 'Here are the values for a and b.'
print 'a: ' + str(record_holder_a)
print 'b: ' + str(record_holder_b)
print 'Their product is ' + str(record_holder_a * record_holder_b)