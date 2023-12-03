import re

def part1(file_path):
    def is_valid(x, y, schematic):
        return 0 <= x < len(schematic) and 0 <= y < len(schematic[0])

    def has_symbol(x, y, length, schematic):
        for dx in [x-1, x+1]:
            if is_valid(dx, y, schematic):
                for dy in range(y, y + length):
                    if is_valid(dx, dy, schematic) and schematic[dx][dy] not in ".0123456789":
                        return True
        for dy in [y-1, y + length]:
            if is_valid(x, dy, schematic):
                for dx in range(x-1, x+2):
                    if is_valid(dx, dy, schematic) and schematic[dx][dy] not in ".0123456789":
                        return True
        return False

    with open(file_path, 'r') as file:
        schematic = [line.strip() for line in file.readlines()]

    total = 0
    for i, line in enumerate(schematic):
        j = 0
        while j < len(line):
            if line[j].isdigit():
                num = re.match(r'\d+', line[j:]).group()
                if has_symbol(i, j, len(num), schematic):
                    total += int(num)
                j += len(num)
            else:
                j += 1
    return total

file_path = 'ques3.txt'
print(part1(file_path))

def part2(file_path):
  from collections import defaultdict
  from re import finditer
  from math import prod

  parts = defaultdict(list)
  with open(file_path, 'r') as file:
      board = file.readlines()

  chars = {(r, c) for r in range(len(board))
                  for c in range(len(board[r].strip()))
                  if board[r][c] not in '0123456789.'}

  for r, row in enumerate(board):
      for m in finditer(r'\d+', row):
          nexts = {(r + s, c + d) for s in (-1, 0, 1) 
                                  for d in (-1, 0, 1)
                                  for c in range(*m.span())}
          for c in nexts & chars:
              parts[c].append(int(m[0]))


  sum_of_gear_ratios = sum(prod(p) for p in parts.values() if len(p) == 2)

  return sum_of_gear_ratios

print(part2(file_path))



