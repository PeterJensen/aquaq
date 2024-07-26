# Author: Peter Jensen

import sys
import itertools

class Config:
  title = "--- Challenge 20: Blackjack ---"
  input = "input-20.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def handValue(hand):
  aces = 0
  value = 0
  for c in hand:
    if c == "A":
      aces += 1
    if c in "23456789":
      value += int(c)
    elif c == "10" or c in "JQK":
      value += 10
  for cc in itertools.combinations_with_replacement((1, 11), aces):
#    print(cc)
    acesValue = sum(cc)
    if acesValue + value == 21:
      return 21
  return aces + value

def solve(lines):
  cards = lines[0].split()
#  cards = ["3", "A",  "K",  "9",  "A",  "7", "4", "9"]
  wins = 0
  hand = []
  for c in cards:
    hand.append(c)
    if handValue(hand) == 21:
      wins += 1
      hand = []
    elif handValue(hand) > 21:
      hand = []
  print("Solution:", wins)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
