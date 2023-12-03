import os
import down

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read().splitlines()
    res1 = 0
    res2 = 0

dx = len(lines)
dy = len(lines[0])
SEEN = []
D = [(1, 0), (0, 1), (1, 1), (-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1)]
for i in range(dx):
    for j in range(dy):
        elem = lines[i][j]
        if not elem.isdigit() and elem != '.':
            STAR = []
            for d in D:
                newi = i+d[0]
                newj = j+d[1]
                if 0 <= i+d[0] < dx and 0 <= j+d[1] < dy:
                    if lines[newi][newj].isdigit() and (newi, newj) not in SEEN:
                        curr = [lines[newi][newj]]
                        SEEN.append((newi, newj))
                        k = 1
                        while True:
                            if 0 <= newj - k and lines[newi][newj - k].isdigit():
                                SEEN.append((newi, newj - k))
                                curr.insert(0, lines[newi][newj - k])
                            else:
                                break
                            k += 1
                        m = 1
                        while True:
                            if newj + m < dy and lines[newi][newj + m].isdigit():
                                SEEN.append((newi, newj + m))
                                curr.append(lines[newi][newj + m])
                            else:
                                break
                            m += 1
                        res1 += int("".join(curr))
                        if elem == "*":
                            STAR.append(int("".join(curr)))
            if STAR and len(STAR) == 2:
                res2 += STAR[0] * STAR[1]

print(f'Result 1 is: {res1}')
print(f'Result 2 is: {res2}')
