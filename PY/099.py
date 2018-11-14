#!/usr/bin/python3

# Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines
# with a base/exponent pair on each line, determine which line number has the greatest numerical value.

filename = 'p099_base_exp.txt'
lines = [line.rstrip('\n') for line in open(filename)]

# Idee: Die Funktion x -> x^(1/n) ist monoton, daher wenden wir sie auf alle Zeilen an, mit n = minimaler Exponent in der Liste

minimal_exponent = 0

for l in lines:
  s = l.split(',')
  b = int(s[1])
  if b < minimal_exponent or minimal_exponent == 0:
    minimal_exponent = b

print('Minimal exponent: ', minimal_exponent)

max = 0
line_number = 0
line_number_max = 0

for l in lines:
  s = l.split(',')
  a = int(s[0])
  b = int(s[1]) / minimal_exponent
  power = a**b
  line_number += 1
  if power > max:
    max = power
    line_number_max = line_number
  
print(line_number_max)