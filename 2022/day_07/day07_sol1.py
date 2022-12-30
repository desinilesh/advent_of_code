import re

INPUT = "input.txt"
SIZE = 100000

root = {}
cwd = {}

def dfs(dir):
    if type(dir) == int:
        return (dir, 0)
    size = 0
    result = 0
    for child in dir.values():
        s, r = dfs(child)
        size += s
        result += r
    if size <= SIZE:
        result += size
    return (size, result)

with open(INPUT, "r") as f:
    data = f.readlines()

for line in data:
    line = line.strip().split()
    if line[0] == "$":
        # Command
        if line[1] == "cd":
            dir = line[2]
            if dir == "/":
                cwd = root
                path = []
            elif dir == "..":
                cwd = path.pop()
            else:
                if dir not in cwd:
                    cwd[dir] = {}
                path.append(cwd)
                cwd = cwd[dir]
    else:
        # Information
        if line[0] == 'dir':
            # Directory name
            if line[1] not in cwd:
                cwd[line[1]] = {}
        else:
            # File size linermation
            cwd[line[1]] = int(line[0])

print(f"Sum of total sizes of those directories = {dfs(root)[1]}")
