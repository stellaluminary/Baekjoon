"""
Method 2

"""

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    visit[x][y] = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and visit[nx][ny]:
            dfs(nx, ny)
    return 1

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
res = 0
for h in range(101):
    cnt = 0
    visit = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if l[i][j] > h:
                visit[i][j] = l[i][j]

    for i in range(n):
        for j in range(n):
            if visit[i][j]:
                cnt += dfs(i,j)

    res = max(res, cnt)
print(res)

"""
Method 3

"""

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y, val):
    visit[x][y] = 1
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if l[nx][ny] > val and visit[nx][ny] == 0:
                dfs(nx, ny, val)
    return 1

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
max_n = max(map(max, l))
res = 0
for h in range(max_n):
    cnt = 0
    visit = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if l[i][j] > h and visit[i][j] == 0:
                cnt += dfs(i, j, h)
    res = max(res, cnt)
print(res)

"""
Method 2

"""
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    visit[x][y] = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and visit[nx][ny]:
            dfs(nx, ny)
    return 1

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
res = 0
for h in range(101):
    cnt = 0
    visit = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if l[i][j] > h:
                visit[i][j] = l[i][j]

    for i in range(n):
        for j in range(n):
            if visit[i][j]:
                cnt += dfs(i,j)

    res = max(res, cnt)
print(res)



