#!/usr/bin/python

# The four adjacent digits in the 1000-digit number that have the greatest product are 9*9*8*9 = 5832.
# [...]
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

num = '73167176531330624919225119674426574742355349194934'
num += '96983520312774506326239578318016984801869478851843'
num += '85861560789112949495459501737958331952853208805511'
num += '12540698747158523863050715693290963295227443043557'
num += '66896648950445244523161731856403098711121722383113'
num += '62229893423380308135336276614282806444486645238749'
num += '30358907296290491560440772390713810515859307960866'
num += '70172427121883998797908792274921901699720888093776'
num += '65727333001053367881220235421809751254540594752243'
num += '52584907711670556013604839586446706324415722155397'
num += '53697817977846174064955149290862569321978468622482'
num += '83972241375657056057490261407972968652414535100474'
num += '82166370484403199890008895243450658541227588666881'
num += '16427171479924442928230863465674813919123162824586'
num += '17866458359124566529476545682848912883142607690042'
num += '24219022671055626321111109370544217506941658960408'
num += '07198403850962455444362981230987879927244284909188'
num += '84580156166097919133875499200524063689912560717606'
num += '05886116467109405077541002256983155200055935729725'
num += '71636269561882670428252483600823257530420752963450'

def prod(list):
  p = 1
  for i in list:
    p *= i
  return p

record = 1
for x in range(0, len(num) - 13):
  product = prod([int(num[i]) for i in range(x, x + 13)])
  if product > record:
    record = product

print(record)