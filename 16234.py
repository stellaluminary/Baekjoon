"""
Method 1

"""
from collections import deque

n,l,r = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    tmp = []
    q = deque()
    q.append((x,y))
    tmp.append((x,y))
    visit[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y +dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if not visit[nx][ny] and l <= abs(c[x][y] - c[nx][ny]) <= r:
                visit[nx][ny] = 1
                q.append((nx,ny))
                tmp.append((nx,ny))
    return tmp

cnt = 0
while 1:
    visit = [[0] * n for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                adj = bfs(i,j)
                if len(adj) > 1:
                    flag = 1
                    val = sum([c[x][y] for x,y in adj]) // len(adj)
                    for x,y in adj:
                        c[x][y] = val

    if not flag:
        break
    cnt += 1
print(cnt)
