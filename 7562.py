"""
Method 3

"""

"""
Method 2

"""


"""
Method 1

"""
from collections import deque
dm = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

def bfs(current, target, cnt, visit):
    q = deque([current])
    visit[current[0]][current[1]] = 1

    while q:
        x, y = q.popleft()

        if [x,y] == target:
            return visit[x][y]

        for i in range(8):
            nx, ny = x+dm[i][0], y+dm[i][1]

            if nx < 0 or ny < 0 or nx >= l or ny >= l:
                continue
            if not visit[nx][ny]:
                visit[nx][ny] = visit[x][y] + 1
                q.append([nx, ny])

for _ in range(int(input())):
    l = int(input())
    present = list(map(int, input().split()))
    target = list(map(int, input().split()))

    visit = [[0]*l for _ in range(l)]
    val = bfs(present, target, 0, visit)
    print(val-1)
