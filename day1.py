'''
Day 1: Report Repair
Url = https://adventofcode.com/2020/day/1
'''

with open('inputs/input1.txt') as file:
   nums = file.readlines()

nums = list(map(int, nums))

for i in nums:
   # --- Part A --- #
   for j in nums:
      if i + j == 2020:
         print(f'{i} + {j} = 2020')
         print(f'{i} * {j} = {i * j}')
   
   # --- Part B --- #
   for j in nums:
      n = i + j
      for x in nums:
         if x + n == 2020:
            print(f'{i} + {j} + {x} = 2020')
            print(f'{i} * {j} * {x} = {i * j * x}')
            exit()
