"""
Method 1

"""
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
x, y, size = 0, 0, 2

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x, y = i, j
            break

def bfs(x,y,size):
    distance = [[0]*n for _ in range(n)]
    visit = [[0]*n for _ in range(n)]
    small_fish = []

    q = deque()
    q.append((x,y))
    visit[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and graph[nx][ny] <= size:
                q.append((nx,ny))
                visit[nx][ny] = 1
                distance[nx][ny] = distance[x][y] + 1
                if 0 < graph[nx][ny] < size:
                    small_fish.append((distance[nx][ny],nx,ny))

    return sorted(small_fish, key=lambda x: (x[0], x[1], x[2]))

time, eat = 0, 0
while 1:
    smf = bfs(x,y,size)

    if len(smf) == 0:
        break

    dist, nx, ny = smf.pop(0)
    graph[x][y], graph[nx][ny] = 0, 0
    time += dist
    eat += 1

    if eat == size:
        size += 1
        eat = 0

    x, y = nx, ny
print(time)



