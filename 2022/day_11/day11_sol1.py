import logging
import re

from collections import deque
from dataclasses import dataclass
from typing import Callable

INPUT = "input.txt"

@dataclass
class Monkey:
    items: deque[int]
    operation: Callable[[int], int]
    div_test: int
    test_true: bool
    test_false: bool
    inspections: int


monkeys = []
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

for _ in range(20):
    for monkey in monkeys:
        while len(monkey.items) > 0:
            item = monkey.items.popleft()
            logging.debug(f"- Monkey inspects item with worry level of {item}")
            worry_level = monkey.operation(item)
            logging.debug(f"- Worry Level is {worry_level} before inspection")
            worry_level //= 3
            logging.debug(f"- Worry Level is {worry_level} after inspection")
            dest_monkey = monkey.test_true if worry_level % monkey.div_test == 0 else monkey.test_false
            logging.debug(f"- Item with worry level {worry_level} is thrown to monkey {dest_monkey}")
            monkeys[dest_monkey].items.append(worry_level)
            monkey.inspections += 1

top_inspections = sorted([monkey.inspections for monkey in monkeys], reverse=True)
print(f"Level of monkey business after 20 rounds = {top_inspections[0] * top_inspections[1]}")
