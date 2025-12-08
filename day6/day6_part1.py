import numpy as np
import time

with open('input.txt') as f:
    lines = f.read().splitlines()

start = time.perf_counter()

operators = lines[-1].split()
values = np.zeros((len(lines)-1, len(operators)))
for i, line in enumerate(lines[:-1]):
    string_values = line.split()
    values[i,:] = [int(val) for val in string_values]

total = 0
for i, operator in enumerate(operators):
    if operator == '*':
        total += np.prod(values[:,i])
    else:
        total += np.sum(values[:,i])

print("Total: %d" % total)
print("Time: %.6f" % (time.perf_counter() - start))