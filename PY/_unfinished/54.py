#!/usr/bin/python

#The file, poker.txt, contains one-thousand random hands dealt to two players.
#Each line of the file contains ten cards (separated by a single space): 
#the first five are Player 1's cards and the last five are Player 2's cards.
# You can assume that all hands are valid (no invalid characters or repeated cards), 
#each player's hand is in no specific order, and in each hand there is a clear winner.
#How many hands does Player 1 win?

from sets import Set

file = '/home/oli/repositories/project_euler/PY/p054_poker.txt'
raw = [x.replace('\n','').split(' ') for x in open(file)]

def isStraight(l):
  for start in xrange(2, 11):
    if Set(l) == Set([start, start+1, start+2, start+3, start+4]) or Set(l) == Set([14, 2, 3, 4, 5]):
      return True
    return False

def evaluate_pair_of_hands(s):
  player1_raw = [s[i] for i in xrange(0, 5)]
  player1_cards = [x[0].replace('T','10').replace('J','11').replace('Q','12').replace('K','13').replace('A','14') for x in player1_raw]
  player1_suits = Set([x[1] for x in player1_raw])

  player2_raw = [s[i] for i in xrange(5, 10)]
  player2_cards = [x[0].replace('T','10').replace('J','11').replace('Q','12').replace('K','13').replace('A','14') for x in player2_raw]
  player2_suits = Set([x[1] for x in player2_raw])

  winner = 0

  # Maximum for straight
  # Broadway: Maximum A, Wheel: Maximum 5
  if Set(player1_cards) == Set([14,2,3,4,5]):
    player1_straightmax = 5
  else:
    player1_straightmax = max(player1_cards)
  if Set(player2_cards) == Set([14,2,3,4,5]):
    player2_straightmax = 5
  else:
    player2_straightmax = max(player2_cards)

  # Straight Flush?
  is_1_winner = False
  is_2_winner = False
  if len(player1_suits) == 1:
    if isStraight(player1_cards):
      is_1_winner = True
  if len(player2_suits) == 1:
    if isStraight(player2_cards):
      is_2_winner = True
  if is_1_winner and is_2_winner:
    if player1_straightmax > player2_straightmax:
      winner = 1
      return winner
    else:
      winner = 2
      return winner
  elif is_1_winner and not is_2_winner:
    winner = 1
    return winner
  elif not is_1_winner and is_2_winner:
    winner = 2
    return winner

  # Full House?


  # Test
  print player1_cards
  print player1_suits

  

print raw[0]
print raw[1]
print raw[2]
print raw[3]
print ' '
print evaluate_pair_of_hands(raw[0])