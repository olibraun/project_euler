#!/usr/bin/python3

# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order 
# the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these 
# four primes, 792, represents the lowest sum for a set of four primes with this property.

# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

import OBMath

def concat(a, b):
  x = str(a) + str(b)
  return int(x)

# Create a dictionary of pairs which tells us if the two numbers and both of their concatenations are prime

# We use the following function in order to have the keys in the dictionary be integers rather than actual pairs - this seems 
# to save some memory.
def indexMap(x, y):
  a = 0
  b = 0
  if x <= y:
    a = x
    b = y
  else:
    a = y
    b = x
  res = int( ( (a+b) * (a+b+1) ) / 2 )
  res += a
  return res


concatenationDicionary = {}
dictionaryLimit = 21000

print('Starting to generate list of primes up to 10000.')
primesUpTo10000 = [x for x in range(1, 30000) if OBMath.isPrime(x)]
print('Prime list generated.')
print(' ')

print('Starting to create prime pair dictionary.')

for i in [x for x in primesUpTo10000 if x <= dictionaryLimit]:
  for j in [x for x in primesUpTo10000 if x >= i and x <= dictionaryLimit]:
    index = indexMap(i, j)
    a = concat(i, j)
    b = concat(j, i)
    if(OBMath.isPrime(a) and OBMath.isPrime(b)):
      concatenationDicionary[index] = 1
    else:
      concatenationDicionary[index] = 0

print(f'Dictionary created up to {dictionaryLimit}.')
print(' ')

# Idea: Any set of five primes satisfying the conditions must contain a set of four primes satisfying the conditions - such as
# 3, 7, 109, 673 as in the introduction.

def searchThree(searchlimit):
  print(f'Searching sets of size 3 in which each element is at most {searchlimit}.')
  threeSets = []
  
  for i in [x for x in primesUpTo10000 if x <= searchlimit]:
    for j in [x for x in primesUpTo10000 if x >= i+1 and x <= searchlimit]:
      for k in [x for x in primesUpTo10000 if x >= j+1 and x <= searchlimit]:
        mySet = [i, j, k]
        
        isValidSet = True
        if concatenationDicionary[indexMap(i, j)] == 0:
          isValidSet = False

        if concatenationDicionary[indexMap(i, k)] == 0:
          isValidSet = False

        if concatenationDicionary[indexMap(j, k)] == 0:
          isValidSet = False
        
        if isValidSet:
          threeSets.append([i, j, k])
  print(f'I have found {len(threeSets)} suitable sets.')
  print(' ')
  return threeSets

def searchFour(threeSets, searchlimit):
  print(f'Searching sets of size 4 in which each element is at most {searchlimit}.')
  fourSets = []

  for s in threeSets:
    lower_limit = max(s) + 1
    for i in [x for x in primesUpTo10000 if x >= lower_limit and x <= searchlimit]:
      mySet = s + [i]
      
      isValidSet = True
      for i in range(4):
        for j in range(i + 1, 4):
          a = mySet[i]
          b = mySet[j]
          index = indexMap(a, b)
          if concatenationDicionary[index] == 0:
            isValidSet = False
            break
      if isValidSet:
        fourSets.append(mySet)
  print(f'I have found {len(fourSets)} suitable sets.')
  print(' ')
  return fourSets

def searchFive(fourSets, searchlimit):
  foundSomething = False
  print(f'Searching sets of size 5 in which each element is at most {searchlimit}.')
  for s in fourSets:
    lower_limit = max(s) + 1
    for i in [x for x in primesUpTo10000 if x >= lower_limit and x <= searchlimit]:
      mySet = s + [i]
      concatenations = []
         
      for x in mySet:
        for y in mySet:
          if x != y:
            concatenations.append(concat(x, y))
          
      isValidSet = True
      for x in concatenations:
        if not OBMath.isPrime(x):
          isValidSet = False
          break
          
      if isValidSet:
        foundSomething = True
        print(f'I have found the set {mySet} with sum {sum(mySet)}.')
  if not foundSomething:
    print('I have not found any suitable sets of size 5.')

threeSets = searchThree(10000)
fourSets = searchFour(threeSets, 20000)
searchFive(fourSets, 20000)