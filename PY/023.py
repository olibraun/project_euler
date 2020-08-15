#!/usr/bin/python

#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# The commented-out solution is disgustingly slow.

def d(n):
  return sum([x for x in range(1, n) if n%x == 0])

def isAbundant(n):
  return d(n) > n

print('Please be patient, this script takes about twenty seconds to run.')

abundant_numbers = [x for x in range(1, 28123 + 1) if isAbundant(x)]

print('Created list of abundant numbers up to 28123.')
print('It has ' + str(len(abundant_numbers)) + ' entries.')

# sums_of_two_abundant_numbers = []
# for x in range(0, len(abundant_numbers)):
#   for y in range(x, len(abundant_numbers)):
#     s = abundant_numbers[x] + abundant_numbers[y]
#     if s <= 28123:
#       to_append = True
#       for l in range(0, len(sums_of_two_abundant_numbers)):
#         if s == sums_of_two_abundant_numbers[l]:
#           to_append = False
#           break
#       if to_append:
#         sums_of_two_abundant_numbers.append(s)

sums_of_two_abundant_numbers = set([])
for x in range(0, len(abundant_numbers)):
  for y in range(x, len(abundant_numbers)):
    s = abundant_numbers[x] + abundant_numbers[y]
    if s <= 28123:
      sums_of_two_abundant_numbers.add(s)

print('Created list of sums of two abundant numbers up to 28123.')
print('It has ' + str(len(sums_of_two_abundant_numbers)) + ' entries.')

non_sums = [x for x in range(1, 28123 + 1) if not x in sums_of_two_abundant_numbers]

print('Here\'s your solution: ' + str(sum(non_sums)))