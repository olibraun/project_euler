import math

class Partitions:
  mydict = {}
  mydict2 = {}

  @staticmethod
  def p(n, m):
    # This returns the number of partions of n whose summands are at most m
    if m == 0:
      return 0
    if n == 0:
      return 1
    if n < 0:
      return 0
    if (n, m-1) not in Partitions.mydict:
      Partitions.mydict[(n, m-1)] = Partitions.p(n, m-1)
    if (n-m, m) not in Partitions.mydict:
      Partitions.mydict[(n-m, m)] = Partitions.p(n-m, m)
    return Partitions.mydict[(n, m-1)] + Partitions.mydict[(n-m, m)]

  @staticmethod
  def generalized_pentagonal(k):
    return int(k * (3*k - 1) / 2)

  @staticmethod
  def fast_p(n):
    # This is based on Euler's pentagonal theorem
    # https://en.wikipedia.org/wiki/Pentagonal_number_theorem
    if n < 0:
      return 0
    if n == 0 or n == 1:
      return 1
    res = 0
    k = 1
    gk = Partitions.generalized_pentagonal(k)
    gkk = Partitions.generalized_pentagonal(-k)
    while n-gk >= 0 or n - gkk >= 0:
      if n-gk not in Partitions.mydict2:
        Partitions.mydict2[n-gk] = Partitions.fast_p(n-gk)
      if n-gkk not in Partitions.mydict2:
        Partitions.mydict2[n-gkk] = Partitions.fast_p(n-gkk)

      res += int((-1)**(k-1)) * Partitions.mydict2[n-gk]
      res += int((-1)**(-k-1)) * Partitions.mydict2[n-gkk]
      
      k += 1
      gk = Partitions.generalized_pentagonal(k)
      gkk = Partitions.generalized_pentagonal(-k)
    return res

def isPrime(n):
  if n < 0:
    n *= -1
  if n == 0:
    return False
  if n == 1:
    return False
  if n == 2:
    return True
  rn = int(math.ceil(math.sqrt(n)))
  for x in range(2, rn + 1):
    if n%x == 0:
      return False
  return True