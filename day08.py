"""
Day 8: Handheld Halting
Url = https://adventofcode.com/2020/day/8
"""
program = []
program_checked = []

with open('inputs/input8.txt') as file:
    input = file.readlines()
    for i in input:
        instruction, nr = i.strip().split()
        program.append((instruction, int(nr)))
        program_checked.append((instruction, int(nr)))
    program.append(('end', 0))
    program_checked.append(('end', 0))


def run_program(program):
    accumulator = 0
    checked = []
    i = 0
    end = False

    while i not in checked:
        line = program[i]
        checked.append(i)

        if line[0] == 'nop':
            i += 1
        elif line[0] == 'acc':
            i += 1
            accumulator += line[1]
        elif line[0] == 'jmp':
            i += line[1]
        elif line[0] == 'end':
            end = True

    return accumulator, end

print(run_program(program)[0])

def program_check():
    program_checked = []
    for line in program:
        program_checked.append(list(line))
    return program_checked

for i, line in enumerate(program):
    if line[0] == 'acc':
        pass

    program_checked = program_check()
    if line[0] == 'nop':
        program_checked[i][0] = 'jmp'
    elif line[0] == 'jmp':
        program_checked[i][0] = 'nop'

    if run_program(program_checked)[1]:
        print(run_program(program_checked)[0])
        break
