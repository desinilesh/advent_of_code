import logging
import re

INPUT = "input.txt"

# Useful for debug
# logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
# logger.setLevel(logging.INFO)

def print_pixel(index, x):
    cycle = index % 40
    if cycle == 0:
        print()
    logger.debug(f"{cycle} - {x}")

    # Print using 2 chars as with 1 it was hard to understand the letter(s)
    if abs(cycle - x) < 2:
        print("##", end='')
    else:
        print("..", end='')

x = 1
index = 0
with open(INPUT, "r") as f:
    data = f.readlines()

for line in data:
    instr_match = re.search(r'(?P<instr>\w+)\s*(?P<add_value>\S+)?', line)
    if instr_match:
        instr = instr_match.group("instr")
        print_pixel(index, x)
        if instr == 'noop':
            logger.debug(f"[{index}] {x} - {instr}")
            index += 1
        elif instr == 'addx':
            add_value = int(instr_match.group("add_value"))
            logger.debug(f"[{index}] {x} - {instr} {add_value}")
            index += 1

            print_pixel(index, x)
            logger.debug(f"[{index}] {x} - {instr} {add_value}")
            x += add_value
            index += 1

logger.debug(f"[{index}] {x} - Final")
print()
