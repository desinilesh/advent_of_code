import re

INPUT = "input.txt"

with open(INPUT, "r") as f:
    data = f.readlines()

aim = 0
x = 0
y = 0
for line in data:
    direction, units = line.split()
    units = int(units)
    match direction:
        case 'forward':
            x += units
            y += aim * units
        case 'down':
            aim += units
        case 'up':
            aim -= units

print(f"Multiplication of final x and y = {x * y}")
