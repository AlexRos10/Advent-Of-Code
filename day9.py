preamble = 25
nums = []
with open("inputs/input9.txt") as file:
    numbers = file.readlines()
    for number in numbers:
        nums.append(int(number))

def factors(numbers, numb):
    for n in numbers:
        if (numb - n) in numbers and n != (numb - n):
            return True
    return False

previous = nums[:preamble]
numbers = nums[preamble:]

for n in numbers:
    if not factors(previous, n):
        solve_a = n
    previous.append(n)
    previous.pop(0)

print(solve_a)

invalid = solve_a
numbers = nums
ahead = numbers.copy()
summed = []
total = 0

for n in numbers:
    total = n
    summed.append(n)
    ahead.pop(0)

    i = 0
    while total < invalid:
        summed.append(ahead[i])
        total += ahead[i]
        i += 1

    if total == invalid:
        print(max(summed) + min(summed))
        break
    
    total = 0
    summed.clear()
