"""
Day 6: Custom Customs
Url = https://adventofcode.com/2020/day/5
"""

with open('inputs/input6.txt') as file:
    answers = file.read()


answers = answers.split('\n\n')
answers_a = []
for answer in answers:
    answer = answer.replace('\n', '')
    answers_a.append(answer)

ans = []
for answer in answers_a:
    answer = "".join(set(answer))
    ans.append(answer)

answers_a = ans
answers_count = 0
for answer in answers_a:
    x = len(answer)
    answers_count += x

print(answers_count)

# --- Part B --- #
answers_count = []

for answer in answers:
    answer = answer.split('\n')
    lenght = len(answer)
    word = "".join(answer)
    answers_b = []
    for i in word:
        count = word.count(i)
        if count == lenght:
            answers_b.append(i)

    answers_b = "".join(set(answers_b))
    answers_count.append(answers_b)

answers_count = "".join(answers_count)
answers_count = len(answers_count)
print(answers_count)