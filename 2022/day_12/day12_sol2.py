from collections import deque

INPUT = "input.txt"

def print_matrix(matrix):
    for row in matrix:
        print(row)

matrix = [list(x) for x in open(INPUT).read().strip().splitlines()]
# print_matrix(matrix)

q = deque()
for r, row in enumerate(matrix):
    for c, item in enumerate(row):
        if item == "S":
            matrix[r][c] = "a"
        if item == "E":
            er = r
            ec = c
            matrix[r][c] = "z"

q.append((0, er, ec))
visited = {(er, ec)}

while q:
    d, r, c = q.popleft()
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if nr < 0 or nc < 0 or nr >= len(matrix) or nc >= len(matrix[0]):
            continue
        if (nr, nc) in visited:
            continue
        if ord(matrix[nr][nc]) - ord(matrix[r][c]) < -1:
            continue
        if matrix[nr][nc] == 'a':
            print(f"The fewest steps from any square with elevation a to location that should get the best signal = {d + 1}")
            exit(0)
        visited.add((nr, nc))
        q.append((d + 1, nr, nc))
