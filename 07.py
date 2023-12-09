import os
import down
from collections import deque, Counter
from copy import deepcopy

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read().splitlines()

res1 = 0
res2 = 0
dict_keys = list(reversed(('7', '6', '5', '4', '3', '2', '1')))
D = {i: deque([]) for i in dict_keys}


def solve(part):

    def compare(prev, cur):
        for val in range(5):
            if cards[prev[val]] > cards[cur[val]]:
                return True
            elif cards[prev[val]] < cards[cur[val]]:
                return False

    if part == 'p1':
        cards = {k: i for i, k in enumerate(list(reversed('A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2'.split(", "))))}
    else:
        cards = {k: i for i, k in enumerate(list(reversed('A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J'.split(", "))))}
    d = {}
    result = 0
    for line in lines:
        a, b = line.split()
        d[a] = int(b)
        if part == 'p1':
            counts = Counter(a)
        else:
            if 'J' in a:
                if len(Counter(a)) == 1:
                    new_a = deepcopy(a)
                elif max(Counter(a), key=Counter(a).get) == 'J':
                    tmp = deepcopy(a).replace('J', '')
                    new_a = a.replace('J', max(Counter(tmp), key=Counter(tmp).get))
                else:
                    new_a = a.replace('J', max(Counter(a), key=Counter(a).get))
            else:
                new_a = deepcopy(a)
            counts = Counter(new_a)
        if len(counts) == 1:
            D['7'].append(a)
        elif max(counts.values()) == 4:
            D['6'].append(a)
        elif max(counts.values()) == 3 and len(counts) == 2:
            D['5'].append(a)
        elif max(counts.values()) == 3 and len(counts) == 3:
            D['4'].append(a)
        elif max(counts.values()) == 2 and len(counts) == 3:
            D['3'].append(a)
        elif max(counts.values()) == 2 and len(counts) == 4:
            D['2'].append(a)
        else:
            D['1'].append(a)

    temp = 1
    for i in dict_keys:
        if D[i]:
            for j in range(1, len(D[i])):
                c = 1
                while True:
                    if j - c < 0:
                        place_item = D[i][j]
                        D[i].remove(D[i][j])
                        D[i].appendleft(place_item)
                        break
                    elif not compare(D[i][j-c], D[i][j]):
                        if c == 1:
                            break
                        place_item = D[i][j]
                        D[i].remove(D[i][j])
                        D[i].insert(j-c+1, place_item)
                        break
                    c += 1
        for elem in D[i]:
            result += temp * d[elem]
            temp += 1
    return result


print(solve('p1'))
print(solve('p2'))
