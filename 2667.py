"""
Method 1
DFS
"""

n=7
l=[[0,1,1,0,1,0,0],
[0,1,1,0,1,0,1],
[1,1,1,0,1,0,1],
[0,0,0,0,1,1,1],
[0,1,0,0,0,0,0],
[0,1,1,1,1,1,0],
[0,1,1,1,0,0,0]]

n = int(input())
l = []
for i in range(n):
     l.append(list(map(int, input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

visit = [[0]*n for _ in range(n)]

def dfs(x, y):
    if x < 0 or x > n-1 or y < 0 or y > n-1:
        return False

    if visit[x][y] == 0 and l[x][y] == 1:
        visit[x][y] = 1
        global cnt
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

res=[]
cnt = 0

for i in range(n):
    for j in range(n):
        if visit[i][j] == 0 and l[i][j] == 1:
            dfs(i, j)
            res.append(cnt)
            cnt = 0

print(len(res))
res.sort()
for x in res:
    print(x)

"""
Method 2 
DFS
"""

n = int(input())
l = []
for i in range(n):
     l.append(list(map(int, input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x, y):
    if x < 0 or x > n-1 or y < 0 or y > n-1:
        return False

    if l[x][y] == 1:
        global cnt
        cnt += 1
        l[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

res=[]
cnt = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            res.append(cnt)
            cnt = 0

res.sort()
print(len(res))
for x in res:
    print(x)

"""
Method 3
BFS
"""

from collections import deque

n = int(input())
l = []
for i in range(n):
     l.append(list(map(int, input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x, y):
    n = len(l)
    queue = deque()
    queue.append((x,y))
    cnt = 1
    l[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1:
                continue

            if l[nx][ny] == 1:
                queue.append((nx, ny))
                l[nx][ny] = 0
                cnt += 1
    return cnt

res=[]

for i in range(n):
    for j in range(n):
        if l[i][j]:
            res.append(bfs(i,j))

res.sort()
print(len(res))
for x in res:
    print(x)










