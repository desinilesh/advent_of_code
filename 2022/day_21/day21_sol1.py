import logging
import re

INPUT = "input.txt"

# Useful for debug
# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

def get_value(monkey):
    if monkey not in monkeys:
        left = get_value(monkey_ops[monkey][0])
        right = get_value(monkey_ops[monkey][2])
        value = eval(f'{left} {monkey_ops[monkey][1]} {right}')
        monkeys[monkey] = int(value)
        logger.debug(f"{monkey} = {value}")
    return monkeys[monkey]

monkeys = {}
monkey_ops = {}
with open(INPUT, "r") as f:
    data = f.readlines()

for i, line in enumerate(data):
    logger.debug(f"[{i}] {line.rstrip()}")
    num_match = re.search(r'(?P<monkey>\w+): (?P<value>\d+)', line)
    if num_match:
        monkeys[num_match.group('monkey')] = int(num_match.group('value'))
        continue
    match = re.search(r'(?P<monkey>\w+): (?P<left>\w+) (?P<op>.) (?P<right>\w+)', line)
    monkey_ops[match.group('monkey')] = [
        match.group('left'), match.group('op'), match.group('right')
    ]

print(f"root = {get_value('root')}")
