# Author: Peter Jensen

import sys

class Config:
  title = "--- Challenge 24: Huff and Puff ---"
  input = "input-24.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

class Node:
  def __init__(self, seq, freq, left = None, right = None):
    self.seq = seq
    self.freq = freq
    self.left = left
    self.right = right
  def __eq__(self, other):
    if other == None:
      return False
    return self.seq == other.seq and self.freq == other.freq
  def __lt__(self, other):
    if self.freq < other.freq:
      return True
    elif self.freq == other.freq:
      if len(self.seq) < len(other.seq):
        return True
      else:
        return ord(self.seq[0]) < ord(other.seq[0])
    return False
  def __repr__(self):
    s = f"{self.seq}:{self.freq}"
    if self.left != None:
      s += f"(left: {self.left}, right: {self.right})"
    return s

def getEncoding(tree, l):
  enc = ""
  n = tree
  while True:
    if n.seq == l:
      break
    else:
      if l in n.left.seq:
        enc += "0"
        n = n.left
      else:
        enc += "1"
        n = n.right
  return enc

def nextLetterCode(code, decodings):
  codes = decodings.keys()
  nlc = ""
  for i in range(len(code)):
    c = code[0:i+1]
    if c in codes and len(c) > len(nlc):
      nlc = c
  return nlc

def insertNode(nodes, node):
  ip = len(nodes)
  for i, n in enumerate(nodes):
    if n.freq > node.freq:
      ip = i
      break
  nodes.insert(ip, node)

def solve(lines):
  letters, code = lines[0:2]
  freqs = {}
  for c in letters:
    freqs[c] = freqs.get(c, 0) + 1
  nodes = [Node(k, v) for k,v in freqs.items()]
  nodes.sort()
  while len(nodes) >= 2:
    l, r = nodes[0:2]
    newNode = Node(l.seq + r.seq, l.freq + r.freq, l ,r)
    nodes = nodes[2:]
    insertNode(nodes, newNode)
  root = nodes[0]
  decodings = {}
  for k in sorted(freqs.keys()):
    encoding = getEncoding(root, k)
    decodings[encoding] = k
  message = ""
  while len(code) > 0:
    c = nextLetterCode(code, decodings)
    if c == "":
      break
    message += decodings[c]
    code = code[len(c):]
  print("Solution:", message)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
