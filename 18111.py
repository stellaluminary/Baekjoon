"""
Method 3

"""

"""
Method 2

"""

import sys
input = sys.stdin.readline

n,m,b = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
res = [1e9, 0]

min_h = min(min(l))
max_h = max(max(l))

for v in range(min_h, max_h + 1):
    up = 0
    down = 0
    time = 0

    for i in range(n):
        for j in range(m):
            diff = l[i][j] - v
            if diff > 0:
                down += diff
            elif diff < 0:
                up -= diff

    if down + b >= up:
        time = down * 2 + up
        if res[0] >= time:
            res[0] = time
            res[1] = v

print(*res)


"""
Method 1

"""

import sys
input = sys.stdin.readline

n,m,b = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
res = [1e9, 0]

min_h = min(min(l))
max_h = max(max(l))

for v in range(min_h, max_h + 1):
    up = 0
    down = 0
    time = 0

    for i in range(n):
        for j in range(m):
            diff = l[i][j] - v
            if diff > 0:
                down += diff
            elif diff < 0:
                up -= diff

    if down + b >= up:
        time = down * 2 + up
        if res[0] >= time:
            res[0] = time
            res[1] = v

print(*res)













