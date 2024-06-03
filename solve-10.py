# Author: Peter Jensen

import sys
import djikstra

class Config:
  title = "--- Challenge 10: Troll Toll ---"
  input = "input-10.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

class Node:
  nextUsers = None
  def __init__(self, user):
    self.user = user
    self.match = self.__eq__
  def __repr__(self):
    return self.user
  def __eq__(self, other):
    return self.user == other.user
  def __hash__(self):
    return hash(self.user)
  def distTo(self, d):
    return self.nextUsers[self.user][d.user]
  def neighbors(self):
    if self.nextUsers.get(self.user) == None:
      return
    for nu in self.nextUsers[self.user].keys():
      yield Node(nu)

def solve(lines):
  nextUsers = {}
  for l in lines[1:]:
    s, d, c = [x for x in l.split(",")]
    if nextUsers.get(s) ==  None:
      nextUsers[s] = {}
    nextUsers[s][d] = int(c)
  Node.nextUsers = nextUsers
#  su = Node("A")
#  eu = Node("E")
  su = Node("TUPAC")
  eu = Node("DIDDY")
#  print(nextUsers)
  dist, prev = djikstra.shortest(su, eu)
  print("Solution:", dist[eu])

def testQ():
  q = djikstra.Queue();
  q.addWithPriority(djikstra.QueueElem('A', 1))
  q.addWithPriority(djikstra.QueueElem('C', 3))
  q.addWithPriority(djikstra.QueueElem('B', 2))
  q.decreasePriority('C', 2)
  print(q)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)
#  testQ()

if __name__ == "__main__":
  main()
