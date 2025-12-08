import time

with open('input.txt') as f:
    lines = f.read().splitlines()

start = time.perf_counter()

count = 0
timelines = 0
beams = {lines[0].find('S'): 1}
lines = [line for line in lines if '^' in line]

for line in lines:
    new_beams = {}
    last_added = None
    for beam in beams:
        timelines = beams[beam]
        if line[beam] == '^':
            count += 1
            new_beams[beam - 1] = new_beams.get(beam - 1, 0) + timelines
            new_beams[beam + 1] = new_beams.get(beam + 1, 0) + timelines
        else:
            new_beams[beam] = new_beams.get(beam, 0) + timelines
    beams = new_beams

print("Beam splits: %d" % count)
print("Timelines: %d" % sum(beams.values()))
print("Time: %.6f" % (time.perf_counter() - start))