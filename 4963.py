"""
Method 2
BFS
"""

import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]

def bfs(x, y, w, h):

    q = deque()
    q.append((x,y))
    island[x][y] = 2

    while q:
        cx, cy = q.popleft()
        for k in range(8):
            nx, ny = cx + dx[k], cy+dy[k]
            if 0 <= nx < h and 0 <= ny < w and island[nx][ny] == 1:
                island[nx][ny] = 2
                q.append((nx, ny))
    return 1

while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    island = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                cnt += bfs(i, j, w, h)
    print(cnt)

"""
Method 1
DFS
"""
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]

def dfs(x, y, w, h):
    island[x][y] = 2
    for k in range(8):
        nx, ny = x + dx[k], y+dy[k]
        if 0 <= nx < h and 0 <= ny < w:
            if island[nx][ny] == 1:
                dfs(nx, ny, w, h)
    return 1

while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    island = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                cnt += dfs(i, j, w, h)
    print(cnt)
