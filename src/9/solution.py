#Advent code challenge day 5 problem 1
'''
import sys

row = 0
col = 0

list_of_seat_ids = []

with open(sys.argv[1]) as f:
    for line in f:
        for i in range(7):
            if line[6-i] == 'B':
                row += 2**i
        for i in range(3):
            if line[9-i] == 'R':
                col += 2**i
        print(f'row = {row} col = {col}')
        list_of_seat_ids.append((row*8) + col)
        row = 0
        col = 0
    
    print(max(list_of_seat_ids))
'''

import sys

LETTER_TO_BINARY = {
    "F": "0",
    "B": "1",
    "L": "0",
    "R": "1",
}
 
def seat_to_binary(seat):
    seat = seat.strip()
    binary_string = [LETTER_TO_BINARY[letter] for letter in seat]
    binary_string = ''.join(binary_string) # ['0', '1', '1', '1'] => '0111'
    return int(binary_string, 2)

with open(sys.argv[1]) as f:
    seat_numbers = [seat_to_binary(seat) for seat in f]

print(max(seat_numbers))