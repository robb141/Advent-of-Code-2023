import os
import down
from collections import deque

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read().splitlines()

DR = len(lines)
DC = len(lines[0])
SEEN = deque([])


def solve(prv, nxt):
    while 0 <= nxt[0] < DR and 0 <= nxt[1] < DC:
        if nxt in SEEN:
            if abs(SEEN.index(nxt) - SEEN.index(prv)) == 1:
                return
        SEEN.append(nxt)
        next_elem = lines[nxt[0]][nxt[1]]
        if nxt[1]-prv[1] == 1:  # to the right
            if next_elem == '/':
                prv, nxt = nxt, (nxt[0]-1, nxt[1])
            elif next_elem == '\\':
                prv, nxt = nxt, (nxt[0]+1, nxt[1])
            elif next_elem == '|':
                solve(nxt, (nxt[0]+1, nxt[1]))
                prv, nxt = nxt, (nxt[0]-1, nxt[1])
            else:
                prv, nxt = nxt, (nxt[0], nxt[1]+1)

        elif nxt[1]-prv[1] == -1:  # to the left
            if next_elem == '/':
                prv, nxt = nxt, (nxt[0]+1, nxt[1])
            elif next_elem == '\\':
                prv, nxt = nxt, (nxt[0]-1, nxt[1])
            elif next_elem == '|':
                solve(nxt, (nxt[0]+1, nxt[1]))
                prv, nxt = nxt, (nxt[0]-1, nxt[1])
            else:
                prv, nxt = nxt, (nxt[0], nxt[1] - 1)

        elif nxt[0]-prv[0] == 1:  # down
            if next_elem == '/':
                prv, nxt = nxt, (nxt[0], nxt[1] - 1)
            elif next_elem == '\\':
                prv, nxt = nxt, (nxt[0], nxt[1] + 1)
            elif next_elem == '-':
                solve(nxt, (nxt[0], nxt[1] + 1))
                prv, nxt = nxt, (nxt[0], nxt[1] - 1)
            else:
                prv, nxt = nxt, (nxt[0] + 1, nxt[1])

        elif nxt[0]-prv[0] == -1:  # up
            if next_elem == '/':
                prv, nxt = nxt, (nxt[0], nxt[1] + 1)
            elif next_elem == '\\':
                prv, nxt = nxt, (nxt[0], nxt[1] - 1)
            elif next_elem == '-':
                solve(nxt, (nxt[0], nxt[1] + 1))
                prv, nxt = nxt, (nxt[0], nxt[1] - 1)
            else:
                prv, nxt = nxt, (nxt[0] - 1, nxt[1])
    return


res2 = 0
for i in range(DR):
    SEEN.clear()
    start = (i, -1)
    start_plus_one = (i, 0)
    solve(start, start_plus_one)
    if start == (0, -1):
        print(f'Result 1 is: {len(set(SEEN))}')
    res2 = max(res2, len(set(SEEN)))

for j in range(DC):
    SEEN.clear()
    start = (-1, j)
    start_plus_one = (0, j)
    solve(start, start_plus_one)
    res2 = max(res2, len(set(SEEN)))

print(f'Result 2 is: {res2}')
