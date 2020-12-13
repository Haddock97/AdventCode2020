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

SEAT_MIN = 8
SEAT_MAX = (2**10) - 8

for num in range(SEAT_MIN, SEAT_MAX):
    if (
        (num not in seat_numbers) and
        (num - 1) in seat_numbers and
        (num + 1) in seat_numbers
    ):
        print(num)

'''
seat_numbers.sort()
for i in range(len(seat_numbers) - 1):
    if seat_numbers[i+1] - seat_numbers[i] == 2:
        print((seat_numbers[i+1] + seat_numbers[i]) / 2)
'''