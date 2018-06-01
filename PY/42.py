#!/usr/bin/python

#The nth term of the sequence of triangle numbers is given by, tn = (1/2)*n(n+1); so the first ten triangle numbers are:
#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we
#form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10. If the word value is a triangle
#number then we shall call the word a triangle word.
#Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand
#common English words, how many are triangle words?

import math

filename = '/home/oli/repositories/project_euler/PY/p042_words.txt'

raw = [x for x in open(filename)]
st = raw[0]
l = st.split(',')
ll = [x.replace('"', '') for x in l]

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def evalWord(st):
  global alphabet
  return sum([alphabet.index(x)+1 for x in st])

def isTriangleNumber(n):
  totest = (math.sqrt(8*n+1) - 1)/2
  return totest.is_integer()

def isTriangleWord(s):
  return isTriangleNumber(evalWord(s))

triangle_words = [1 for word in ll if isTriangleWord(word)]
print sum(triangle_words)