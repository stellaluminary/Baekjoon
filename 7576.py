"""
Method 1
BFS
"""
m,n=6,4
l=[
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1],
]

l=[
[0, -1, 0, 0, 0, 0],
[-1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1],
]
#
# l=[
# [1, -1, 0, 0, 0, 0],
# [0, -1, 0, 0, 0, 0],
# [0, 0, 0, 0, -1, 0],
# [0, 0, 0, 0, -1, 1],
# ]
#
# m,n = 5,5
# l=[
# [-1, 1, 0, 0, 0],
# [0, -1, -1, -1, 0],
# [0, -1, -1, -1, 0],
# [0, -1, -1, -1, 0],
# [0, 0, 0, 0, 0]
# ]

# m,n=2,2
# l=[[1,-1],
#    [-1,1]]

from collections import deque
import sys
input = sys.stdin.readline

m,n = map(int, input().split())
l = []
q = deque()

for i in range(n):
    l.append(list(map(int, input().split())))
    for j in range(m):
        if l[i][j] == 1:
            q.append((i,j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                continue

            if l[nx][ny] == 0:
                l[nx][ny] = l[x][y] + 1
                q.append((nx, ny))

bfs()
ans = 0
for i in l:
    for j in i:
        if j ==0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))

print(ans - 1)


"""
Method 2
BFS 92%에서 런타임에러 UnboundLocalError
"""

from collections import deque
import sys
input = sys.stdin.readline

m,n = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(one_loc):
    q = deque()
    for i in range(len(one_loc)):
        q.append(one_loc[i])

    while q:
        x, y, c = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                continue

            if l[nx][ny] == 0:
                l[nx][ny] = 1
                q.append((nx, ny, c+1))
    return c

one_loc = []
for i in range(n):
    for j in range(m):
        if l[i][j] == 1:
            one_loc.append((i,j,0))

cnt = bfs(one_loc)

for i in l:
    if 0 in i:
        print(-1)
        exit(0)

print(cnt)


