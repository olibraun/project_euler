#!/usr/bin/python

#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
#numbers.txt

filename = '/home/oli/repositories/project_euler/13_PY/numbers.txt'

# with open() as f:
#   lines = f.readlines()

lines = [line.rstrip('\n') for line in open(filename)]

sum = 0
for l in lines:
  sum += int(l)

sum_str = str(sum)
res_str = ''

for x in xrange(0, 10):
  res_str += sum_str[x]

print res_str