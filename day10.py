"""
Day 10: Adapter Array
Url = https://adventofcode.com/2020/day/10
"""

with open('input10.txt') as file:
    numbers = file.readlines()

adapters = []
for i in numbers:
    adapters.append(int(i))

adapters.sort()
jolt = 0
one_diff = 0
three_diff = 1
for i in adapters:
    if i - jolt == 1:
        one_diff += 1
    elif i - jolt == 3:
        three_diff += 1
    
    jolt = i

print(one_diff * three_diff)

adapters.append(max(adapters) + 3)
paths = [1, 1, 2]
use_path = [False] * (adapters[-1] + 1)
for i in adapters:
    use_path[i] = True

for i in range(3, len(use_path)):
    p = paths[2] + paths[1] + paths[0]
    paths[0] = paths[1]
    paths[1] = paths[2]
    paths[2] = p * use_path[i]

print(paths[2])
