#!/usr/bin/python3

file = open("/home/oliver/repositories/project_euler/PY/p059_cipher.txt")
txt = ""
for x in file:
  txt += x

def charToAscii(s):
  return ord(s)

def stringToAscii(s):
  return ''.join(str(ord(c)) for c in s)

def AsciiToString(a):
  return chr(a)

print(stringToAscii("Hello world"))
print(stringToAscii('Hello again'))


txt = txt.split(',')
txt = [int(x.replace('\n','')) for x in txt]

plain_alphabet = [AsciiToString(n) for n in range(stringToAscii("a"), stringToAscii("z") + 1)]
ascii_alphabet = [stringToAscii(x) for x in plain_alphabet]

print(ascii_alphabet)

# for x in txt:
#   print(AsciiToString(x))