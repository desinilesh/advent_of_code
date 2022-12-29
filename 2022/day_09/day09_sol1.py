import re

INPUT = "input.txt"

head = [0, 0]
tail = [0, 0]
visited = set()

visited.add(tuple(tail))

with open(INPUT, "r") as f:
    data = f.readlines()

for line in data:
    direction, steps = line.split()
    for _ in range(int(steps)):
        match direction:
            case 'D':
                head[1] -= 1
            case 'U':
                head[1] += 1
            case 'L':
                head[0] -= 1
            case 'R':
                head[0] += 1

        diff_x = head[0] - tail[0]
        diff_y = head[1] - tail[1]

        if abs(diff_x) > 1 or abs(diff_y) > 1:
            if diff_x == 0:
                tail[1] += diff_y // 2
            elif diff_y == 0:
                tail[0] += diff_x // 2
            else:
                tail[0] += 1 if diff_x > 0 else -1
                tail[1] += 1 if diff_y > 0 else -1

        visited.add(tuple(tail))

print(f"Number of unique positions visited by tail = {len(visited)}")
