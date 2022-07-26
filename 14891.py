"""
Method 3

"""

"""
Method 2

"""
from collections import deque

def rotate_right(x, d):
    if x > 4 or gears[x - 1][2] == gears[x][6]:
        return

    if gears[x - 1][2] != gears[x][6]:
        rotate_right(x + 1, -d)
        gears[x].rotate(d)

def rotate_left(x, d):
    if x < 1 or gears[x][2] == gears[x + 1][6]:
        return

    if gears[x][2] != gears[x + 1][6]:
        rotate_left(x - 1, -d)
        gears[x].rotate(d)

gears = {}
for i in range(1, 5):
    gears[i] = deque((map(int, input())))

for _ in range(int(input())):
    x, d = map(int, input().split())

    rotate_right(x + 1, -d)
    rotate_left(x - 1, -d)
    gears[x].rotate(d)

ans = 0
for i in range(4):
    ans += gears[i + 1][0] * (2 ** i)
print(ans)

"""
Method 1

"""
import copy
s = [[]]+[list(map(int, input())) for _ in range(4)]

for i in range(int(input())):
    n, d = map(int, input().split())
    t = copy.deepcopy(s)
    if d == 1:
        t[n] = [s[n][-1]] + s[n][:-1]
    else:
        t[n] = s[n][1:] + [s[n][0]]
    rot = d
    for i in range(n,4):
        rot = rot * -1
        if s[i][2] != s[i+1][6]:
            if rot == 1:
                t[i+1] = [s[i+1][-1]] + s[i+1][:-1]
            else:
                t[i+1] = s[i+1][1:] + [s[i+1][0]]
        else:
            break

    rot = d
    for i in range(n, 1, -1):
        rot = rot * -1
        if s[i-1][2] != s[i][6]:
            if rot == 1:
                t[i-1] = [s[i-1][-1]] + s[i-1][:-1]
            else:
                t[i-1] = s[i-1][1:] + [s[i-1][0]]
        else:
            break
    s = copy.deepcopy(t)

ans = 0
for i in range(1,5):
    ans += 2**(i-1) * s[i][0]
print(ans)








