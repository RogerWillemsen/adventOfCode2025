import time
from functools import cache

with open('input.txt') as f:
    lines = f.read().splitlines()

start = time.perf_counter()

servers = {}
for line in lines:
    parts = line.split(':')
    servers[parts[0]] = [p for p in parts[1].strip().split(' ')]

@cache
def count_next_server(value, has_visited_dac, has_visited_fft):
    next_servers = servers[value]
    count = 0
    for next_server in next_servers:
        if next_server == 'out':
            count += 1 if has_visited_dac and has_visited_fft else 0
        else:
            count += count_next_server(next_server, has_visited_dac or next_server == 'dac', has_visited_fft or next_server == 'fft')
    return count

count1 = count_next_server('you', True, True)
count2 = count_next_server('svr', False, False)

print("Paths part 1: %d" % count1)
print("Paths part 2: %d" % count2)
print("Time: %.6f" % (time.perf_counter() - start))




