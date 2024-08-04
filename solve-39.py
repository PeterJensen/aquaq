# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge 39: Game of Throwns ---"
  input = "input-39.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def throw3(throw, throws, currentPlayer, playerTotals):
  pt = playerTotals[currentPlayer]
  for t in range(throw, min(throw+3, len(throws))):
    pt += throws[t]
    if pt == 501:
      break
  playerTotals[currentPlayer] = pt
  return t+1, pt

def solve(lines):
  throws = [int(n) for n in lines[0].split()]
  playerTotals = [0, 0]
  finalDartsSum = 0
  player0Wins = 0
  throw = 0
  firstPlayer = 0  
  currentPlayer = 0
  while throw < len(throws):
    throw, points = throw3(throw, throws, currentPlayer, playerTotals)
    if points == 501:
      finalDartsSum += throws[throw-1]
#      print(f"{currentPlayer}: finalDart: {throws[throw-1]}")
      if currentPlayer == 0:
        player0Wins += 1
      playerTotals = [0, 0]
      firstPlayer = 1 if firstPlayer == 0 else 0
      currentPlayer = firstPlayer
    else:
      currentPlayer = 1 if currentPlayer == 0 else 0
#  print(f"player0Wins: {player0Wins}, finalDartsSum: {finalDartsSum}")
  print("Solution:", player0Wins*finalDartsSum)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
