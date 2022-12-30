import re

INPUT = "input.txt"
TOTAL_DISK_SPACE = 70_000_000
UPDATE_SPACE = 30_000_000

root = {}
cwd = {}

def size(dir):
    if type(dir) == int:
        return dir
    return sum(map(size, dir.values()))

def dfs(dir, space):
    result = TOTAL_DISK_SPACE
    if size(dir) >= space:
        result = size(dir)
    for child in dir.values():
        if type(child) == int:
            continue
        candidate = dfs(child, space)
        result = min(result, candidate)
    return result

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

space = size(root) - TOTAL_DISK_SPACE + UPDATE_SPACE
print(f"Size of smallest directory to be deleted to free up enough space to run update = {dfs(root, space)}")
