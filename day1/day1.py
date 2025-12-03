import pandas as pd
import time

# Part 1 & 2
with open('input.txt') as f:
    lines = f.read().splitlines()

start = time.perf_counter()
position = 50
count1, count2 = 0, 0
for line in lines:
    direction = -1 if line[0] == 'L' else 1
    change = int(line[1:])
    new_position = position + change * direction
    if new_position <= 0 and position != 0:
        count2 += (int(abs(new_position) / 100) + 1)
    elif new_position <= 0 and change >= 100:
        count2 += int(abs(new_position) / 100)
    elif new_position >= 100:
        count2 += int(new_position / 100)
    position = new_position % 100
    if position == 0:
        count1 += 1

print("Code part 1: %d" % count1)
print("Code part 2: %d" % count2)
print("Time: %.6f" % (time.perf_counter() - start))

# Part 1 using pandas (slow)
df = pd.read_csv('input.txt', header=None, names=['dial'])
start = time.perf_counter()
df['dial_numeric'] = df['dial'].apply(lambda x: int(x.replace('L', '-').replace('R', '')))
df['dial_position'] = df['dial_numeric'].cumsum()
df['dial_position'] = df['dial_position'].apply(lambda x: (x + 50) % 100)
code = df[df['dial_position']==0]['dial_position'].count()

print("Code: %d" % code)
print("Time: %.6f" % (time.perf_counter() - start))