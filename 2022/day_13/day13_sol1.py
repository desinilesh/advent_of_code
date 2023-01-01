import ast
import sys

INPUT = "input.txt"

# Return of negative values imply that it is the right order
def compare(left, right):
    if isinstance(left, int):
        if isinstance(right, int):
            # Both are ints
            return left - right
        else:
            # left is int, right is list
            return compare([left], right)
    elif isinstance(right, int):
        # left is list, right is int
        return compare(left, [right])

    # left and right are list
    for l, r in zip(left, right):
        cmp = compare(l, r)
        if cmp:
            return cmp
    return len(left) - len(right)

packets = []
with open(INPUT, "r") as f:
    data = f.readlines()

for line in data:
    if not line.strip():
        continue
    packets.append(ast.literal_eval(line.strip()))

sum_of_pair_indices = 0
for i in range(0, len(packets), 2):
    sum_of_pair_indices += i//2 + 1 if compare(packets[i], packets[i + 1]) < 0 else 0
print(f"Sum of indices of pairs in right order = {sum_of_pair_indices}")
