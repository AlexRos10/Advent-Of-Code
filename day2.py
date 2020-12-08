"""
Day 2: Password Philosophy
Url = https://adventofcode.com/2020/day/2
"""
with open('inputs/input2.txt') as file:
    passwords = file.readlines()

def check_passwords(passwords):
    valid_passwords_a = 0
    valid_passwords_b = 0

    for i in range(len(passwords)):
        # --- Formating the string to operate with it --- #
        n = passwords[i].replace(':', '')
        password_conditions = n.split(' ')
        nums = password_conditions[0]
        nums = nums.split('-')
        rules = []
        rules.append(int(nums[0]))
        rules.append(int(nums[1]))
        rules.append(password_conditions[1]) 
        rules.append(password_conditions[2])
        # --- Part A --- #
        password = rules[3]
        letter = password.count(rules[2])
        if letter >= (rules[0]) and letter <= rules[1]:
            valid_passwords_a += 1
        # -- Part B --- #
        letter = rules[2]
        if password[(rules[0] - 1)] == letter and password[(rules[1] - 1)] != letter or password[(rules[0] - 1)] != letter and password[(rules[1] - 1)] == letter:
            valid_passwords_b += 1

    print(valid_passwords_a)
    print(valid_passwords_b)

check_passwords(passwords)
