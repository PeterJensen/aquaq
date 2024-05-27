# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge 07: What is best in life? ---"
  input = "input-07.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

class Game:
  def __init__(self, a, b, score):
    self.a = a
    self.b = b
    self.score = score
  def __repr__(self):
    return f"W: {self.winner()} L: {self.loser()}";
  def winner(self):
    return self.a if self.score[0] > self.score[1] else self.b
  def loser(self):
    return self.a if self.score[1] > self.score[0] else self.b

def parse(lines):
  games = []
  for l in lines[1:]:
    a, b, score = l.split(",")
    games.append(Game(a, b, [int(p) for p in score.split("-")]))
  return games

def solve(lines):
  games = parse(lines)
  # initialize rankings
  rankings = {}
  for g in games:
    rankings[g.winner()] = 1200
    rankings[g.loser()] = 1200
  for g in games:
    w = g.winner()
    l = g.loser()
    ew = 1 / (1 + 10**((rankings[l]-rankings[w])/400))
    d = 20*(1-ew)
    rankings[w] = rankings[w] + d
    rankings[l] = rankings[l] - d
  #print(rankings)
  result = int(max(rankings.values())) - int(min(rankings.values()))
  print(f"Solution: {result}")

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
