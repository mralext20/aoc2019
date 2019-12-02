#!/usr/bin/env python
import math


def fuel_needed(module_mass: int) -> int:
    w = math.floor(module_mass/ 3) - 2
    # print(f"in: {module_mass}, w: {w}")
    if w > 0:
        return w + fuel_needed(w) or 0
    return 0


masses = open("input.txt", 'r')
total = 0
for i in masses.readlines():
    mass = fuel_needed(int(i))
    total += mass

print(total)
