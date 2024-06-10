import sys

def getLines():
  file = "input-30.txt" if len(sys.argv) < 2 else sys.argv[1]
  return None if file == "" else [l.strip() for l in open(file, 'r').readlines()]

def count_winning_positions(deck: str) -> int:
    ones = deck.count("1")
    if ones % 2 == 1:
        return ones // 2 + 1

    return 0


def solution(lines) -> int:
    return sum(count_winning_positions(line) for line in lines)


assert count_winning_positions("11010") == 2
assert count_winning_positions("110") == 0
assert count_winning_positions("00101011010") == 3

print("Solution", solution(getLines()))