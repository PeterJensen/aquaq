# Author: Peter Jensen

import sys
from datetime import date

class Config:
  title = "--- Challenge 17: The Beautiful Shame ---"
  input = "input-17.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def daysBetween(fromTo):
  d1 = date.fromisoformat(fromTo[0])
  d2 = date.fromisoformat(fromTo[1])
  d = d2 - d1
  return d.days

def toYMD(ds):
  return ''.join([c if c != "-" else '' for c in ds])

def solve(lines):
  scores = []
  for l in lines[1:]:
    fields = l.split(",")
    if len(fields) <= 3:
      team, d, score = fields
      scores.append((d, team, score))
    else:
      d, hteam, ateam, hscore, ascore, *_ = fields
      scores.append((d, hteam, hscore))
      scores.append((d, ateam, ascore))
#  print(scores)
  zeroScores = dict()
  maxRanges  = dict()
  for d, team, score in scores:
    if score == "0":
      if not team in zeroScores.keys():
        zeroScores[team] = d
    else:
      if team in zeroScores.keys():
        if team in maxRanges.keys():
          mr = daysBetween(maxRanges[team])
          nr = daysBetween((zeroScores[team], d))
          if nr > mr:
            maxRanges[team] = (zeroScores[team], d)
        else:
          maxRanges[team] = (zeroScores[team], d)
        del zeroScores[team]
  zeroStreak = 0
  maxZeroTeam = None
#  print(maxRanges)
  for t, mr in maxRanges.items():
    db = daysBetween(mr)
    if db > zeroStreak:
      maxZeroTeam = (t, mr)
      zeroStreak = db
  print("Solution:", f"{maxZeroTeam[0]} {toYMD(maxZeroTeam[1][0])} {toYMD(maxZeroTeam[1][1])}")

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
