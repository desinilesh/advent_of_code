import re

from dataclasses import dataclass
from functools import cache
# from pprint import pprint

INPUT = "input.txt"
PARSER = re.compile(r"Valve (?P<name>\w+) has flow rate=(?P<rate>\d+); .+[valve]s? (?P<neighbors>.+)$")

@dataclass
class Valve:
    name: str
    rate: int
    neighbors: list[str]

@cache
def dfs(opened, mins_remaining, curr_valve_name):
    if mins_remaining <= 0:
        return 0

    most_released_pressure = 0
    curr_valve = cave[curr_valve_name]
    for neighbor in curr_valve.neighbors:
        most_released_pressure = max(most_released_pressure, dfs(opened, mins_remaining - 1, neighbor))

    if curr_valve_name not in opened and curr_valve.rate > 0 and mins_remaining > 0:
        opened = set(opened)
        opened.add(curr_valve_name)
        mins_remaining -= 1
        total_released_pressure = mins_remaining * curr_valve.rate

        for neighbor in curr_valve.neighbors:
            most_released_pressure = max(most_released_pressure, total_released_pressure + dfs(frozenset(opened), mins_remaining - 1, neighbor))
    return most_released_pressure

with open(INPUT, "r") as f:
    data = f.readlines()

cave = {}
for line in data:
    match = re.search(PARSER, line)
    if not match:
        continue
    name = match.group("name")
    cave[name] = Valve(name, int(match.group("rate")), [neighbor.strip() for neighbor in match.group("neighbors").split(",")])
# pprint(cave)
print(dfs(frozenset(), 30, "AA"))
