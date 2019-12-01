#!/usr/bin/env python
import math

masses = open("input.txt", 'r')
total = 0
for i in masses.readlines():
    mass = int(i)
    fuel = math.floor(mass / 3) - 2
    total += fuel

print(total)