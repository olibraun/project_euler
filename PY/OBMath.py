class Partitions:
  mydict = {}

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