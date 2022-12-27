import sys

from collections import deque

INPUT = "input.txt"
NUM_DISTINCT_CHARS = 4

with open(INPUT, "r") as f:
    line = f.readline()

max_n = deque(maxlen=NUM_DISTINCT_CHARS)
for index, char in enumerate(line):
    max_n.append(char)
    if len(set(max_n)) == NUM_DISTINCT_CHARS:
        print(f"Number of chars before first start-of-packet marker {index + 1}")
        exit(0)
