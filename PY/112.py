#!/usr/bin/python3

# Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
# Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
# We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
# Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. 
# In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.
# Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.
# Find the least number for which the proportion of bouncy numbers is exactly 99%.

def is_increasing(n):
  sn = str(n)
  for i in range(0, len(sn)-1):
    if(sn[i+1] < sn[i]):
      return False
  return True

def is_decreasing(n):
  sn = str(n)
  for i in range(0, len(sn)-1):
    if(sn[i+1] > sn[i]):
      return False
  return True

def is_bouncy(n):
  return not is_decreasing(n) and not is_increasing(n)

proportion = 0
n = 1
number_of_bouncy_numbers = 0

while proportion < 0.99:
  if is_bouncy(n):
    number_of_bouncy_numbers += 1
  proportion = number_of_bouncy_numbers / n
  n += 1

print(n-1)
