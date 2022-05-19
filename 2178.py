"""
Method 1
BFS
"""
n,m=4, 6
l=[
    [1,0,1,1,1,1],
    [1,0,1,0,1,0],
    [1,0,1,0,1,1],
    [1,1,1,0,1,1]
]

l = [
    [1,1,0,1,1,0],
    [1,1,0,1,1,0],
    [1,1,1,1,1,1],
    [1,1,1,1,0,1]
]

n,m = 7,7
l=[
[1,0,1,1,1,1,1],
[1,1,1,0,0,0,1],
[1,0,0,0,0,0,1],
[1,0,0,0,0,0,1],
[1,0,0,0,0,0,1],
[1,0,0,0,0,0,1],
[1,1,1,1,1,1,1],
]

from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().strip())))

visit = [[0]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visit[x][y] = 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                continue

            if visit[nx][ny] != 0:
                visit[nx][ny] = min(visit[nx][ny], visit[x][y] + 1)

            if l[nx][ny] and visit[nx][ny] == 0:
                q.append((nx,ny))
                visit[nx][ny] = visit[x][y] + 1

bfs(0,0)
print(visit[n-1][m-1])

"""
Method 2
BFS
"""

from collections import deque
import sys
input = sys.stdin.readline

# n,m = map(int, input().split())
# l = []
# for i in range(n):
#     l.append(list(map(int, input().strip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                continue

            if l[nx][ny] == 1:
                q.append((nx,ny))
                l[nx][ny] = l[x][y] + 1

bfs(0,0)
print(l[n-1][m-1])


"""
Method 3
DFS 실패 - 주변탐색이 어려움
"""
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().strip())))

visit = [[0]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y, prev):
    if x == n-1 and y==m-1:
        visit[x][y] = prev + 1
        return True

    if l[x][y] == 1 and visit[x][y] == 0:
        visit[x][y] = prev + 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                continue
            if visit[nx][ny] < prev and visit[nx][ny] != 0:
                prev = visit[nx][ny]
                visit[x][y] = prev + 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <0 or nx >n-1 or ny < 0 or ny > m-1:
                continue

            dfs(nx, ny, visit[x][y])
        return True
    return False

dfs(0, 0, 0)
print(visit[n-1][m-1])
























