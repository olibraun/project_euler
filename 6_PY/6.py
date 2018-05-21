#!/usr/bin/python

#The sum of the squares of the first ten natural numbers is 12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_of_squares = sum([i**2 for i in xrange(1, 101)])
square_of_sum = (100*101/2)**2

print square_of_sum - sum_of_squares