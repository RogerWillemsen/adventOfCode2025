import math
import numpy as np
import time

with open('input.txt') as f:
    lines = f.read().splitlines()

# Read data
ranges = []
ids = []
for line in lines:
    if '-' in line:
        start, end = line.split('-')
        ranges.append((int(start), int(end)))
    elif len(line) == 0:
        continue
    else:
        ids.append(int(line))

# Prepare data
ids = np.reshape(np.array(ids), (-1, len(ids))).T
ranges = np.array(ranges)
range_start = ranges[:, 0]
range_end = ranges[:, 1]

start = time.perf_counter()
in_range = range_end - range_start >= np.abs(range_start + range_end - 2 * ids)
count = np.count_nonzero(np.sum(in_range, axis=1))

print("Number of fresh ingredient ids: %d" % count)
print("Time: %.6f" % (time.perf_counter() - start))

## Alternative part 1 solution, based on part 2 (slightly faster)

start = time.perf_counter()

# Sort
ids = ids + np.zeros((1,2))
ids [:, 1] = math.inf
extended_ranges = np.concatenate((ids, ranges))
order = np.argsort(extended_ranges[:, 0])
extended_ranges = extended_ranges[order]

count = 0
range_end = 0
for i in range(len(extended_ranges)):
    if extended_ranges[i, 1] == math.inf:
        if extended_ranges[i, 0] <= range_end:
            count += 1
        else:
            continue
    elif extended_ranges[i, 1] >= range_end:
        range_end = extended_ranges[i, 1]

print("Number of fresh ingredient ids: %d" % count)
print("Time: %.6f" % (time.perf_counter() - start))