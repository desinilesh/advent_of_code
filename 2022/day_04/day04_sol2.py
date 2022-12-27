import re

INPUT = "input.txt"
PATTERN = re.compile(r'(\d+)-(\d+),(\d+)-(\d+)')

with open(INPUT, "r") as f:
    data = f.readlines()

num_overlaps = 0
for line in data:
    low1, high1, low2, high2 = map(int, re.match(PATTERN, line).groups())
    if (low1 <= low2) and (low2 <= high1) or \
       (low2 <= low1) and (low1 <= high2):
        num_overlaps +=1
print(f"[PART 2] Number of overlaps = {num_overlaps}")
