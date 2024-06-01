# Author: Peter Jensen

import sys
from collections import defaultdict
import djikstra
from threading import Thread
from multiprocessing import Process, Queue

class Config:
  title = "--- Challenge 15:  ---"
  input = "input-15.txt"
  words = "words.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def getWords():
  return [l.strip() for l in open(Config.words, 'r').readlines()]

def diff(w1, w2):
  d = 0
  for i in range(len(w1)):
    d += 1 if w1[i] != w2[i] else 0
  return d

class Node:
  nextWords  = None
  def __init__(self, w):
    self.word = w
    self.match = self.__eq__
  def __repr__(self):
    return self.word
  def __eq__(self, other):
    return self.word == other.word
  def __hash__(self):
    return hash(self.word)
  def length(self):
    return len(self.word)
  def neighbors(self):
    for nw in self.nextWords[self.word]:
      yield Node(nw)

def chainLen(sn, en, wordsByLen):
  nextWords = {}
  wl = sn.length()
  for w in wordsByLen[wl]:
    nextWords[w] = {ww for ww in wordsByLen[wl] if diff(w, ww) == 1}
  Node.nextWords = nextWords
  dist, prev = djikstra.shortest(sn, en)
  return dist[en] + 1

def solve(lines):
  words = getWords()
  wordsByLen = defaultdict(list)
  for w in words:
    wordsByLen[len(w)].append(w)
  p = 1
  for l in lines:
    s, e = [w for w in l.split(",")]
    cl = chainLen(Node(s), Node(e), wordsByLen)
    print(f"{s} -> {e}: {cl}")
    p *= cl 
  print("Solution:", p)

prods = None
def chainLenThread(i, sn, en, wordsByLen):
  global prods
  prods[i] = chainLen(sn, en, wordsByLen)
  print(f"{sn} -> {en}: {prods[i]}")

def chainLenProcess(q, sn, en, wordsByLen):
#  global prods
#  prods[i] = chainLen(sn, en, wordsByLen)
#  print(f"{sn} -> {en}: {prods[i]}")
  prod = chainLen(sn, en, wordsByLen)
  q.put((f"{sn}", f"{en}", prod))

def solveWithThreads(lines):
  global prods
  words = getWords()
  wordsByLen = defaultdict(list)
  for w in words:
    wordsByLen[len(w)].append(w)
  threads = []
  prods = [None for _ in range(len(lines))]
  for i, l in enumerate(lines):
    s, e = [w for w in l.split(",")]
    threads.append(Thread(target = chainLenThread, args=(i, Node(s), Node(e), wordsByLen)))
  for t in threads:
    t.start()
  for t in threads:
    t.join()
  print(prods)
  print("Solution:", )

def solveWithProcesses(lines):
  words = getWords()
  wordsByLen = defaultdict(list)
  for w in words:
    wordsByLen[len(w)].append(w)
  processes = []
  q = Queue()
  for i, l in enumerate(lines):
    s, e = [w for w in l.split(",")]
    processes.append(Process(target = chainLenProcess, args=(q, Node(s), Node(e), wordsByLen)))
  for p in processes:
    p.start()
  prod = 1
  for _ in processes:
    sn, en, cl = q.get()
    prod *= cl
    print(f"{sn} -> {en}: {cl}")
  for p in processes:
    p.join()
  print("Solution:", prod)

def main():
  print(Config.title)
  lines = getLines()
  #solve(lines)
  #solveWithThreads(lines)
  solveWithProcesses(lines)

if __name__ == "__main__":
  main()
