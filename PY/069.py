#!/usr/bin/python

#Find the value of n <= 1,000,000 for which n/phi(n) is a maximum.

print 'The value of n/phi(n) depends only on the primes involved in a factorizaion of n, without exponents.'
print 'Since p^k / phi(p^k) = p / (p-1), we just need to find the largest number of the form 2*3*5*7*... which is below 1,000,000.'
print 'The solution is 2*3*5*7*11*13*17 = ' + str(2*3*5*7*11*13*17) + '.'