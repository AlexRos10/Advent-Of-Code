"""
Day 3: Toboggan Trajectory
Url = https://adventofcode.com/2020/day/3
"""

with open('inputs/input3.txt') as file:
    map = file.readlines()
    map = [line.strip() for line in map]

# --- Part A --- #
treecount = 0
row, col = 0, 0

while row + 1 < len(map):
    row += 1
    col += 3
    space = map[row][col % len(map[row])]
    if space == '#':
        treecount += 1

print(treecount)

# --- Part B --- #
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
total = 1

for slope in slopes:
    treecount = 0
    row, col = 0, 0

    while row + 1 < len(map):
        row += slope[1]
        col += slope[0]
        space = map[row][col % len(map[row])]
        if space == '#':
            treecount += 1
    
    total *= treecount

print(total)