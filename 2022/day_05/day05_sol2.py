import re

from collections import deque

INPUT = "input.txt"
with open(INPUT, "r") as f:
    data = f.readlines()

s = []
stacks = deque()

is_move_cmd = False
for line in data:
    if line.isspace():
        is_move_cmd = True
        num_stacks = int(s.pop()[-1])
        for col in range(num_stacks):
            crates = deque()
            for row in range(len(s)):
                if len(s[row]) <= col or s[row][col] == " ":
                    continue
                value = s[row][col]
                crates.append(value)
            stacks.append(crates)
    elif not is_move_cmd:
        s.append(line[1::4])
    else:
        num_items, src_col, dst_col = map(int, re.findall("\d+", line))
        crate_mover_9000 = deque()
        for _ in range(num_items):
            crate = stacks[src_col - 1].popleft()
            crate_mover_9000.append(crate)
        for _ in range(num_items):
            crate = crate_mover_9000.pop()
            stacks[dst_col - 1].appendleft(crate)

print("Crates on top of each stack: ", end='')
for stack in stacks:
    print(stack[0], end='')
print()
