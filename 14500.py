"""
Method 3

"""

# https://jshong1125.tistory.com/20

# https://jeongchul.tistory.com/670

n, m = map(int, input().split())
t = []
for i in range(n):
    t.append(list(map(int, input().split())))

ans = []
for i in range(n):  # 세로
    for j in range(m):  # 가로
        if j+3 < m:
            ans.append(t[i][j]+t[i][j+1]+t[i][j+2]+t[i][j+3])

        if i+3 < n:
            ans.append(t[i][j]+t[i+1][j]+t[i+2][j]+t[i+3][j])

        if j+1 < m and i+1 < n:  # 정사각형
            ans.append(t[i][j]+t[i+1][j]+t[i][j+1]+t[i+1][j+1])

        if j+1 < m and i+2 < n:
            ans.append(t[i][j] + t[i+1][j] + t[i+2][j] + t[i+2][j+1])
            ans.append(t[i][j] + t[i][j+1] + t[i+1][j+1] + t[i+2][j+1])
            ans.append(t[i][j+1] + t[i+1][j+1] + t[i+2][j] + t[i+2][j+1])
            ans.append(t[i][j] + t[i][j+1] + t[i+1][j] + t[i+2][j])
            ans.append(t[i][j] + t[i+1][j] + t[i+1][j+1] + t[i+2][j+1])
            ans.append(t[i][j+1] + t[i+1][j] + t[i+1][j+1] + t[i+2][j])
            ans.append(t[i][j] + t[i+1][j] + t[i+1][j+1] + t[i+2][j])
            ans.append(t[i][j+1] + t[i+1][j] + t[i+1][j+1] + t[i+2][j+1])

        if j+2<m and i+1<n:
            ans.append(t[i][j] + t[i+1][j] + t[i][j+1] + t[i][j+2])
            ans.append(t[i+1][j] + t[i+1][j+1] + t[i+1][j+2] + t[i][j+2])
            ans.append(t[i][j] + t[i][j+1] + t[i][j+2] + t[i+1][j+2])
            ans.append(t[i][j] + t[i+1][j] + t[i+1][j+1] + t[i+1][j+2])
            ans.append(t[i+1][j] + t[i+1][j+1] + t[i][j+1] + t[i][j+2])
            ans.append(t[i][j] + t[i][j+1] + t[i+1][j+1] + t[i+1][j+2])
            ans.append(t[i][j] + t[i][j+1] + t[i+1][j+1] + t[i][j+2])
            ans.append(t[i+1][j] + t[i][j+1] + t[i+1][j+1] + t[i+1][j+2])

print(max(ans))

"""
Method 2

"""

import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y, step, tot):
    global n, m, ans, max_val

    if tot + max_val * (4 - step) <= ans:
        return

    if step == 4:
        ans = max(ans, tot)
        return

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
            if step == 2:
                visit[nx][ny] = 1
                dfs(x, y, step + 1, tot+a[nx][ny])
                visit[nx][ny] = 0
            visit[nx][ny] = 1
            dfs(nx, ny, step+1, tot+a[nx][ny])
            visit[nx][ny] = 0

n,m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
ans = 0
max_val = max(map(max, a))

for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i, j, 1, a[i][j])
        visit[i][j] = 0
print(ans)

"""
Method 1

"""

import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y, step, tot):
    global n, m, ans, max_val

    if tot + max_val * (4 - step) <= ans:
        return

    if step == 4:
        ans = max(ans, tot)
        return

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visit[nx][ny]:
                visit[nx][ny] = 1
                dfs(nx, ny, step+1, tot+a[nx][ny])
                visit[nx][ny] = 0

def adj(x,y):
    global n, m, ans
    t = []
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            t.append(a[nx][ny])
    if len(t) >= 3:
        tmp = a[x][y] + sum(sorted(t, reverse=True)[:3])
        ans = max(ans, tmp)

n,m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
ans = 0
max_val = max(map(max, a))

for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i, j, 1, a[i][j])
        visit[i][j] = 0
        adj(i, j)

print(ans)



