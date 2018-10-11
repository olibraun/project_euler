#!/usr/bin/python3

# A common security method used for online banking is to ask the user for three random characters from a passcode.
# For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
# The text file, keylog.txt, contains fifty successful login attempts.
# Given that the three characters are always asked for in order, analyse the file so as to determine 
# the shortest possible secret passcode of unknown length.

#from sets import set

filename = 'p079_keylog.txt'
lines = [line.rstrip('\n') for line in open(filename)]

before_map = {}
after_map = {}

for l in lines:
  a = int(l[0])
  b = int(l[1])
  c = int(l[2])

  if a not in after_map:
    after_map[a] = set((b,))
  else:
    after_map[a].add(b)
  
  if b not in before_map:
    before_map[b] = set((a,))
  else:
    before_map[b].add(a)

  if b not in after_map:
    after_map[b] = set((c,))
  else:
    after_map[b].add(c)
  
  if c not in before_map:
    before_map[c] = set((b,))
  else:
    before_map[c].add(b)

# Find all digits occuring in the code
digit_set_1 = set(before_map.keys())
digit_set_2 = set(after_map.keys())
digit_set = digit_set_1.union(digit_set_2)

# Find first digit of the code
firstdigit = -1
for i in digit_set:
  if i not in before_map:
    firstdigit = i

codes = set(())
codes.add(firstdigit)

# Find the subsequent digits
done = False

while not done:
  done = True
  newcodes = codes.copy()
  for code in codes:
    newcodes.remove(code)
    lastletter = str(code)[-1]
    if int(lastletter) in after_map:
      done = False
      next_letters = after_map[int(lastletter)]
      for next in next_letters:
        newcode = code * 10 + next
        newcodes.add(newcode)
    else:
      newcodes.add(code)
    codes = newcodes


# Filter for those candidates which contain all digits
codes = [x for x in codes if set(int(y) for y in str(x)) == digit_set]
print(codes)
