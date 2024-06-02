# Author: Peter Jensen

import sys
from copy import copy

class Config:
  title = "--- Challenge 37: GUESS WORDS ---"
  input = "input-37.txt"
  words = "words.txt"

def getLines():
  file = Config.input if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def getWords():
  return [l.strip() for l in open(Config.words, 'r').readlines()]

def wordSum(w):
  return sum([ord(c) - ord('a') for c in w])

def canMatch(word, guess, score):
#  print(word, guess, score)
  scoreInt = [int(s) for s in score.split(" ")]
  guessList = [g for g in guess]
  wordList  = [w for w in word]
  # check direct matches
  for i, s in enumerate(scoreInt):
    if s == 2:
      if guess[i] != word[i]:
        return False
      wordList[i] = " "
  # check that there aren't matching letters where they're not supposed to be
  for i, s in enumerate(scoreInt):
    if (s == 0 or s == 1) and guess[i] == word[i]:
      return False
  # check that letters in wrong position is in the word
  for i, s in enumerate(scoreInt):
    inWord = False
    if s == 1:
      if guess[i] == wordList[i]:
        return False
      for wi, c in enumerate(wordList):
        if guess[i] == c and i != wi:
          wordList[wi] = " "
          inWord = True
          break
      if not inWord:
        return False
  # check that letters that's not suppose to be in word isn't there
  for i, s in enumerate(scoreInt):
    if s == 0:
      if guess[i] in wordList:
        return False
  return True

def solve(lines):
  wordsOrg = [w for w in getWords() if len(w) == 5]
  words = copy(wordsOrg)
  s = 0
  for l in lines[1:]:
    if len(l) == 0:
      break
    guess, score = l.split(",")
    words = [w for w in words if canMatch(w, guess, score)]
#    print(guess, score)
#    print(words)
#    print(len(words))
    if len(words) == 1:
      print(words[0])
      s += wordSum(words[0])
      words = copy(wordsOrg)
    if len(words) == 0:
      print(guess, score)
  print("Solution:", s)

def main():
  print(Config.title)
  lines = getLines()
  solve(lines)

if __name__ == "__main__":
  main()
