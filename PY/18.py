#!/usr/bin/python

#By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#[...]
#That is, 3 + 7 + 4 + 9 = 23.
#Find the maximum total from top to bottom of the triangle below:
#[...]
#NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
#However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
#it cannot be solved by brute force, and requires a clever method! ;o)

sample_triangle = []
sample_triangle.append('3'.split(' '))
sample_triangle.append('7 4'.split(' '))
sample_triangle.append('2 4 6'.split(' '))
sample_triangle.append('8 5 9 3'.split(' '))
sample_triangle = [[int(n) for n in line] for line in sample_triangle]

triangle = []
triangle.append('75'.split(' '))
triangle.append('95 64'.split(' '))
triangle.append('17 47 82'.split(' '))
triangle.append('18 35 87 10'.split(' '))
triangle.append('20 04 82 47 65'.split(' '))
triangle.append('19 01 23 75 03 34'.split(' '))
triangle.append('88 02 77 73 07 63 67'.split(' '))
triangle.append('99 65 04 28 06 16 70 92'.split(' '))
triangle.append('41 41 26 56 83 40 80 70 33'.split(' '))
triangle.append('41 48 72 33 47 32 37 16 94 29'.split(' '))
triangle.append('53 71 44 65 25 43 91 52 97 51 14'.split(' '))
triangle.append('70 11 33 28 77 73 17 78 39 68 17 57'.split(' '))
triangle.append('91 71 52 38 17 14 91 43 58 50 27 29 48'.split(' '))
triangle.append('63 66 04 68 89 53 67 30 73 16 69 87 40 31'.split(' '))
triangle.append('04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'.split(' '))
triangle = [[int(n) for n in line] for line in triangle]

#Work from the bottom to the top and use the rule "a -> a + max(b, c)"
#The the result should appear at the top

def do_it(list):
  for i in xrange(len(list) - 2, -1, -1):
    for j in xrange(0, len(list[i])):
      temp = list[i][j]
      newval = temp + max([list[i+1][j], list[i+1][j+1]])
      list[i][j] = newval

do_it(triangle)
print triangle[0][0]