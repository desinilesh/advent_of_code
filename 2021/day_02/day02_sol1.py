import re

INPUT = "input.txt"

with open(INPUT, "r") as f:
    data = f.readlines()

x = 0
y = 0
for line in data:
    direction, units = line.split()
    units = int(units)
    match direction:
        case 'forward':
            x += units
        case 'down':
            y += units
        case 'up':
            y -= units

print(f"Multiplication of final x and y = {x * y}")
