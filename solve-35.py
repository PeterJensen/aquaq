# Author: Peter Jensen

import sys
import re

class Config:
  title = "--- Challenge 35: Columns ---"
  input = "input-35.txt"
  words = "words.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def getWords():
  return [l.strip() for l in open(Config.words, 'r').readlines()]

class Enigma:
  def __init__(self, keyword):
    self.keyword = keyword
    sk = sorted(keyword)
    co = []
    for c in keyword:
      i = sk.index(c)
      co.append(sk.index(c))
      sk[i] = None
    self.columnOrder = co

  def encode(self, s):
    kwl = len(self.keyword)
    psl = len(s) % kwl
    if psl != 0:
      psl = kwl - psl
    ps = s + " "*psl
    columns = [[] for _ in range(kwl)]
    for ci in range(kwl):
      for c in range(ci, len(ps), kwl):
        columns[ci].append(ps[c])
    es = [None for _ in range(kwl)]
    for ci in range(kwl):
      es[self.columnOrder[ci]] = columns[ci]
    return "".join(["".join(c) for c in es])

  def decode(self, s):
    kwl = len(self.keyword)
    cols = [None for _ in range(kwl)]
    cl = (len(s) + kwl - 1) // kwl
#    print(f"len(s): {len(s)}, kwl: {kwl}, cl: {cl}")
    for i in range(kwl):
      cols[i] = s[i*cl:i*cl+cl]
    cols[kwl-1] += " "*(kwl*cl - len(s))
    ocols = []    
    for i in range(kwl):
      ocols.append(cols[self.columnOrder[i]])
    return "".join(["".join([ocols[c][i] for c in range(kwl)]) for i in range(cl)])

def solve(lines):
#  enigma = Enigma("GLASS")
#  es = enigma.encode("WE ARE DISCOVERED FLEE AT ONCE")
#  print(es)
#  ds = enigma.decode(es)
#  print(ds)
#  return
  solution = None
  for i, w in enumerate(getWords()):
    if i % 1000 == 0:
      print(f"{i}: {w}")
    enigma = Enigma(w)
    ds = enigma.decode(lines[0][:-1])
#    if ds.find("  ") == -1:
#    if ds.find(" are ") != -1 and ds.find(" is ") != -1 and ds.find("she ") != -1 and ds.find("he ") != -1:
    if re.search("\\.[a-zA-Z]", ds) == None:
      print(f"{i}: {w}")
      print(ds)
      solution = w
      break
  print("Solution:", solution)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
