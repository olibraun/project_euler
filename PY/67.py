#!/usr/bin/python

file = '/home/oli/repositories/project_euler/PY/p067_triangle.txt'
raw = [x.replace('\n', '').split(' ') for x in open(file)]
triangle = [[int(n) for n in l] for l in raw]

#Use the function from problem 18
def do_it(list):
  for i in xrange(len(list) - 2, -1, -1):
    for j in xrange(0, len(list[i])):
      temp = list[i][j]
      newval = temp + max([list[i+1][j], list[i+1][j+1]])
      list[i][j] = newval

do_it(triangle)
print triangle[0][0]