#!/usr/bin/python3

# The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 
# (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
# Find the smallest cube for which exactly five permutations of its digits are cube.

def getUniquePermutation(n):
  sn = str(n)
  sna = [x for x in sn]
  sna.sort(reverse=True)
  return int(''.join(sna))

n = 345
cache = {}
while True:
  nn = n**3
  p = getUniquePermutation(nn)
  if p in cache:
    cache[p].add(nn)
  else:
    cache[p] = set([nn])
  if len(cache[p]) == 5:
    print(f'I have found suitable cube, the minimum permutation is {min(cache[p])}.')
    break
  n+=1