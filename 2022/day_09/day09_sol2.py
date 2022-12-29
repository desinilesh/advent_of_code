import re

INPUT = "input.txt"
NUM_ROPE_KNOTS = 10

rope = [[0, 0] for _ in range(NUM_ROPE_KNOTS)]
visited = set()

visited.add(tuple(rope[-1]))

with open(INPUT, "r") as f:
    data = f.readlines()

for line in data:
    direction, steps = line.split()
    for _ in range(int(steps)):
        match direction:
            case 'D':
                rope[0][1] -= 1
            case 'U':
                rope[0][1] += 1
            case 'L':
                rope[0][0] -= 1
            case 'R':
                rope[0][0] += 1

        for i in range(NUM_ROPE_KNOTS - 1):
            head = rope[i]
            tail = rope[i + 1]

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

        visited.add(tuple(rope[-1]))

print(f"Number of unique positions visited by tail with 10 knots = {len(visited)}")
