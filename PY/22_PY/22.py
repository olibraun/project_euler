#!/usr/bin/python

#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it
#into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical
#position in the list to obtain a name score.
#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
#So, COLIN would obtain a score of 938 * 53 = 49714.
#What is the total of all the name scores in the file?

filename = '/home/oli/repositories/project_euler/PY/22_PY/p022_names.txt'

raw = [x for x in open(filename)]
st = raw[0]
l = st.split(',')
ll = [x.replace('"', '') for x in l]
ll.sort()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def evalName(st):
  global alphabet
  return sum([alphabet.index(x)+1 for x in st])

totalScore = 0

for i in xrange(0, len(ll)):
  totalScore += (i+1)*evalName(ll[i])

print totalScore