import logging
import re

INPUT = "input.txt"

# Useful for debug
# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
# logger.setLevel(logging.INFO)

def sum_signal_strengths(signals):
    return sum([ i * signals[i] for i in range(20, 221, 40) ])

x = 1
values = [x, x]
index = 1
with open(INPUT, "r") as f:
    data = f.readlines()

for line in data:
    instr_match = re.search(r'(?P<instr>\w+)\s*(?P<add_value>\S+)?', line)
    if instr_match:
        instr = instr_match.group("instr")
        if instr == 'noop':
            logger.debug(f"[{index}] {x} - {instr}")
            values.append(x)
            index += 1
        elif instr == 'addx':
            add_value = int(instr_match.group("add_value"))
            logger.debug(f"[{index}] {x} - {instr} {add_value}")
            values.append(x)
            index += 1
            logger.debug(f"[{index}] {x} - {instr} {add_value}")
            x += add_value
            values.append(x)
            index += 1
logger.debug(f"[{index}] {x} - Final")
print(sum_signal_strengths(values))
