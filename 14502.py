"""
Method 1

"""

from collections import deque
from itertools import combinations
import copy
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        table[x][y] = 2

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0<=nx<n and 0<=ny<m:
                if table[nx][ny] == 0:
                    table[nx][ny] = 2
                    q.append((nx,ny))

n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

zero_loc = []
for i in range(n):
    for j in range(m):
        if l[i][j] == 0:
            zero_loc.append((i,j))

three_loc = list(combinations(zero_loc, 3))

res = []
for tl in three_loc:
    table = copy.deepcopy(l)
    for idx in tl:
        table[idx[0]][idx[1]] = 1

    for i in range(n):
        for j in range(m):
            if table[i][j] == 2:
                bfs(i, j)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if table[i][j] == 0:
                cnt += 1

    res.append(cnt)

print(max(res))



"""
Method 2

"""


from collections import deque
from itertools import combinations
import copy
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        table[x][y] = 2

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0<=nx<n and 0<=ny<m:
                if table[nx][ny] == 0:
                    table[nx][ny] = 2
                    q.append((nx,ny))

n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

zero_loc = []
for i in range(n):
    for j in range(m):
        if l[i][j] == 0:
            zero_loc.append((i,j))

three_loc = list(combinations(zero_loc, 3))

res = []
for tl in three_loc:
    table = copy.deepcopy(l)
    for idx in tl:
        table[idx[0]][idx[1]] = 1

    for i in range(n):
        for j in range(m):
            if table[i][j] == 2:
                bfs(i, j)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if table[i][j] == 0:
                cnt += 1

    res.append(cnt)

print(max(res))


"""
Method 3

시간초과

"""
from collections import deque
import copy
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()

    table = copy.deepcopy(l)

    for i in range(n):
        for j in range(m):
            if table[i][j] == 2:
                q.append((i,j))

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0<=nx<n and 0<=ny<m and table[nx][ny] == 0:
                table[nx][ny] = 2
                q.append((nx,ny))

    global ans
    cnt = 0

    for i in range(n):
        cnt += table[i].count(0)

    ans = max(ans, cnt)

def rec_wall(num):
    if num == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):

            if l[i][j] == 0:
                l[i][j] = 1
                rec_wall(num + 1)
                l[i][j] = 0

n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

ans = 0
rec_wall(0)
print(ans)