#!/usr/bin/python

#In England the currency is made up of pound, L, and pence, p, and there are eight coins in general circulation:
#1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).
#It is possible to make L2 in the following way:
#1*L1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p
#How many different ways can L2 be made using any number of coins?

coins = [1, 2, 5, 10, 20, 50, 100, 200]

count = 0

a = 200
while a >= 0:
  b = a
  while b >= 0:
    c = b
    while c >= 0:
      d = c
      while d >= 0:
        e = d
        while e >= 0:
          f = e
          while f >= 0:
            g = f
            while g >= 0:
              count += 1
              g -= 2
            f -= 5
          e -= 10
        d -= 20
      c -= 50
    b -= 100
  a -= 200

print(count)