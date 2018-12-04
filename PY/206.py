# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
# where each "_" is a single digit.

SEARCH_LIMIT = 1389026624  # This is the square root of 1929394959697989990
for n in range(1010101010, SEARCH_LIMIT):
  if n % 10 != 0:
    continue
  pre_test = str(((n % 1000000000)**2 % 1000000000))
  if pre_test[0] != '6' or pre_test[2] != '7' or pre_test[4] != '8' or pre_test[6] != '9':
    continue
  print(f'Testing {n}.')
  nn = n**2
  snn = str(nn)
  if len(snn) != 19:
    continue
  if snn[0] != '1':
    continue
  if snn[2] != '2':
    continue
  if snn[4] != '3':
    continue
  if snn[6] != '4':
    continue
  if snn[8] != '5':
    continue
  if snn[10] != '6':
    continue
  if snn[12] != '7':
    continue
  if snn[14] != '8':
    continue
  if snn[16] != '9':
    continue
  if snn[18] != '0':
    continue
  print(n, nn)
  break