"""
Method 1
BFS
"""

t = 2
m,n,k = 10,8,17

l=[[1,0,0,0,0,0,0,0],
   [1,1,0,0,0,0,0,0],
   [0,0,0,0,1,0,0,0],
   [0,0,0,0,1,0,0,0],
   [0,0,1,1,0,1,0,0],
   [0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0],
   [0,0,0,0,1,1,1,0],
   [0,0,0,0,1,1,1,0],
   [0,0,0,0,1,1,1,0]
   ]

from collections import deque
import sys
input = sys.stdin.readline
t = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    l[x][y]=0

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > m-1 or ny < 0 or ny > n-1:
                continue

            if l[nx][ny]:
                l[nx][ny]=0
                q.append((nx,ny))
    return True

for v in range(t):
    m, n, k = map(int, input().split())
    l = [[0] * n for _ in range(m)]
    for i in range(k):
        a, b = map(int, input().split())
        l[a][b] = 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            if l[i][j]:
                cnt += bfs(i, j)
    print(cnt)


"""
Method 2
DFS
"""

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
t = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    if x < 0 or x > m - 1 or y < 0 or y > n - 1:
        return False

    if l[x][y]:
        l[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > m-1 or ny < 0 or ny > n-1:
                continue
            dfs(nx, ny)
        return True
    return False

for v in range(t):
    m,n,k = map(int, input().split())
    l=[[0]*n for _ in range(m)]
    for i in range(k):
        a,b = map(int, input().split())
        l[a][b] = 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            if l[i][j]:
                cnt += dfs(i,j)
    print(cnt)



