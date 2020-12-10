"""
Day 5: Binary Boarding
Url = https://adventofcode.com/2020/day/5
"""
with open('inputs/input5.txt') as file:
    places = file.readlines()

def check_seat(a : int, b : int, up : str, down : str, h : int, seat : str):
    for i in seat:
        if i == up:
            a = a
            if int(b/2) <= a:
                b = int((b - (b - a)/2))
            else:
                b = int(b/2)

        if i == down:
            b = b
            if h != 0:
                a += int(int(b - a)/2) + 1
            else:
                a = int(b/2) + 1

            h = 1

        if b == a:
            return b

highest_seat_id = 0
for place in places:
    row = check_seat(0, 127, 'F', 'B', 0, place[0:7])
    column = check_seat(0, 7, 'L', 'R', 0, place[7::])
    seat_id = row * 8 + column
    if seat_id >= highest_seat_id:
        highest_seat_id = seat_id

print(highest_seat_id)

def get_seat_id(place):
    row = check_seat(0, 127, 'F', 'B', 0, place[0:7])
    column = check_seat(0, 7, 'L', 'R', 0, place[7::])
    seat_id = row * 8 + column
    return seat_id

possible_ids = [i for i in range(1024)]
for place in places:
    possible_ids.remove(get_seat_id(place))

possible_ids = ['1', '2', '3', '4', '5', '727', '928', '929']

for i in range(len(possible_ids)):
    if int(possible_ids[i - 1]) != int(possible_ids[i]) - 1 and int(possible_ids[i + 1]) != int(possible_ids[i]) + 1:
        possible_id = possible_ids[i]
        print(possible_id)
        break
