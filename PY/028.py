#!/usr/bin/python

#Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#21 22 23 24 25
#20  7  8  9 10
#19  6  1  2 11
#18  5  4  3 12
#17 16 15 14 13
#It can be verified that the sum of the numbers on the diagonals is 101.
#What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

grid_size = 1001

number = 1
length = 2
diagonals = [1]

while number < grid_size**2:
  for i in range(0, 4):
    number += length
    diagonals.append(number)
  length += 2

print sum(diagonals)