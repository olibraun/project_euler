#!/usr/bin/python3

# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
# Not all numbers produce palindromes so quickly. For example,

# 349 + 943 = 1292,
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337

# That is, 349 took three iterations to arrive at a palindrome.
# Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. 
# A number that never forms a palindrome through the reverse and add process is called a Lychrel number. 
# Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is 
# Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become 
# a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map 
# it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a 
# palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).
# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.
# How many Lychrel numbers are there below ten-thousand?

def LychrelStep(n):
  rn = int(str(n)[::-1])
  return n + rn

def isPalindrome(n):
  return str(n) == str(n)[::-1]

def IsLychrel(n):
  orig_n = n
  res = True
  iterations = 0
  while(iterations < 55):
    n = LychrelStep(n)
    iterations += 1
    if(isPalindrome(n)):
      res = False
      break
  # print(f'{orig_n} checked in {iterations} iterations, result {res}.')
  return res

assert(not IsLychrel(47))
assert(not IsLychrel(349))
assert(not IsLychrel(943))
assert(IsLychrel(4994))
assert(IsLychrel(196))

number = len([x for x in range(0, 10000) if IsLychrel(x)])
print(number)