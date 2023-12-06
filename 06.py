import os
import down

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read().splitlines()
    res1 = 1

time = [int(x) for x in lines[0].split()[1:]]
distance = [int(x) for x in lines[1].split()[1:]]

time2 = int("".join([x for x in lines[0].split()[1:]]))
distance2 = int("".join([x for x in lines[1].split()[1:]]))

for i, t in enumerate(time):
    c = 0
    for j in range(1, t-1):
        temp = (t - j) * j
        if temp > distance[i]:
            c += 1
    res1 *= c

res2 = 0
for j in range(1, time2-1):
    temp = (time2 - j) * j
    if temp > distance2:
        res2 += 1

print(f'Result 1 is: {res1}')
print(f'Result 2 is: {res2}')
