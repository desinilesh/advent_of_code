import logging
import re

from collections import deque
from dataclasses import dataclass
from math import gcd
from typing import Callable

INPUT = "input.txt"

# Get Least Common Multiple
def get_lcm(nums):
    lcm = 1
    for i in nums:
        lcm = lcm*i//gcd(lcm, i)
    return lcm

@dataclass
class Monkey:
    items: deque[int]
    operation: Callable[[int], int]
    div_test: int
    test_true: bool
    test_false: bool
    inspections: int

monkeys = []
div_tests = []

with open(INPUT, "r") as f:
    data = f.read()

for block in data.split("\n\n"):
    lines = block.splitlines()

    items = deque(map(int, lines[1].split(": ")[1].split(", ")))

    op = lines[2].split("= ")[1]
    operation = eval(f"lambda old: {op}")

    div_test = int(lines[3].split()[-1])

    test_true = int(lines[4].split()[-1])

    test_false = int(lines[5].split()[-1])

    monkeys.append(Monkey(items, operation, div_test, test_true, test_false, 0))
    div_tests.append(div_test)

lcm = get_lcm(div_tests)

for i in range(10000):
    if (i + 1) % 1000 == 0:
        logging.debug(f"== After round {i + 1} ==")
    for monkey in monkeys:
        while len(monkey.items) > 0:
            item = monkey.items.popleft()
            worry_level = monkey.operation(item) % lcm
            dest_monkey = monkey.test_true if worry_level % monkey.div_test == 0 else monkey.test_false
            monkeys[dest_monkey].items.append(worry_level)
            monkey.inspections += 1
        if (i + 1) % 1000 == 0:
            logging.debug(f"Monkey {i} inspected items {monkey.inspections} times.")

top_inspections = sorted([monkey.inspections for monkey in monkeys], reverse=True)
print(f"Level of monkey business after 10000 rounds = {top_inspections[0] * top_inspections[1]}")
