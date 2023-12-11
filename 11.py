import os
import down

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read().splitlines()

DR = len(lines)
DC = len(lines[0])
empty_row = []
empty_column = [i for i in range(DC)]
points = []

for i in range(DR):
    if '#' not in lines[i]:
        empty_row.append(i)
        continue
    for j in range(DC):
        elem = lines[i][j]
        if elem == '#':
            points.append((i, j))
            if j in empty_column:
                empty_column.remove(j)

res1 = 0
res2 = 0
p_len = len(points)
for i in range(p_len-1):
    cur = points[i]
    for j in range(i+1, p_len):
        new = points[j]
        empty_1 = 0
        empty_2 = 0
        for r in range(min(new[0], cur[0]), max(new[0], cur[0])):
            if r in empty_row:
                empty_1 += 1
                empty_2 += 999999
        for c in range(min(new[1], cur[1]), max(new[1], cur[1])):
            if c in empty_column:
                empty_1 += 1
                empty_2 += 999999
        res1 += empty_1 + abs(new[0] - cur[0]) + abs(new[1] - cur[1])
        res2 += empty_2 + abs(new[0] - cur[0]) + abs(new[1] - cur[1])

print(f'Result 1 is: {res1}')
print(f'Result 2 is: {res2}')
