import numpy as np
import time

with open('input.txt') as f:
    lines = f.read().splitlines()

start = time.perf_counter()

operators = lines[-1]

total = 0
skip = False
values = []
for i, operator in enumerate(operators[::-1]):
    if skip:
        skip = False
        continue

    value = ''
    for line in lines[:-1]:
        value += line[len(operators) - 1 -i]
    values.append(int(value))

    if operator != ' ':
        skip = True
        if operator == '*':
            total += np.prod(values)
        else:
            total += np.sum(values)
        values = []


print("Total: %d" % total)
print("Time: %.6f" % (time.perf_counter() - start))