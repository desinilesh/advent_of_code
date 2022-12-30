import re

INPUT = "input1.txt"
CUBE_SIDES = 6

with open(INPUT, "r") as f:
    data = f.readlines()

cubes = []
for line in data:
    x, y, z = map(int, line.split(','))
    cubes.append((x, y, z))

total_visible_sides = 0
for cube in cubes:
    # Number of visible sides of current cube
    v = CUBE_SIDES

    x, y, z = cube

    v -= 1 if (x+1, y,   z)   in cubes else 0
    v -= 1 if (x,   y+1, z)   in cubes else 0
    v -= 1 if (x,   y,   z+1) in cubes else 0
    v -= 1 if (x-1, y,   z)   in cubes else 0
    v -= 1 if (x,   y-1, z)   in cubes else 0
    v -= 1 if (x,   y,   z-1) in cubes else 0

    total_visible_sides += v

print(f"Total visible sides from all cubes = {total_visible_sides}")
