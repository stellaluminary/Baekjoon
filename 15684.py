"""
Method 2
시간 초과
"""
n, m, h = map(int, input().split())
visited = [[False] * (n+1) for _ in range(h+1)]
combi = []
for _ in range(m):
    a, b = map(int, input().split())
    visited[a][b] = True

def check():
    for i in range(1, n+1):
        now = i
        for j in range(1, h+1):
            if visited[j][now-1]:
                now -= 1
            elif visited[j][now]:
                now += 1
        if now != i:
            return False
    return True

def dfs(depth, idx):
    global answer
    if depth >= answer:
        return
    if check():
        answer = depth
        return

    for c in range(idx, len(combi)):
        x, y = combi[c]
        if not visited[x][y-1] and not visited[x][y+1]:
            visited[x][y] = True
            dfs(depth+1, c+1)
            visited[x][y] = False

for i in range(1,h+1):
    for j in range(1, n):
        if not visited[i][j-1] and not visited[i][j] and not visited[i][j+1]:
            combi.append([i, j])

answer = 4
dfs(0, 0)

print(answer if answer < 4 else -1)

"""
Method 1
시간 초과
"""

def check():
    for col in range(n):
        y = col
        for x in range(h):
            if board[x][y]:
                y += 1
            elif y > 0 and board[x][y-1]:
                y -= 1
        if y != col:
            return False
    return True

def dfs(cnt, x, y):
    global ans
    if check():
        ans = min(ans, cnt)
        return
    if cnt == 3 or ans <= cnt:
        return
    for i in range(x, h):
        k = y if i == x else 0
        for j in range(k, n-1):
            if j > 0 and board[i][j-1]:
                continue
            if not board[i][j] and not board[i][j+1]:
                board[i][j] = 1
                dfs(cnt+1, i, j+2)
                board[i][j] = 0

n,m,h = map(int, input().split())
board = [[0]*n for _ in range(h)]
for _ in range(m):
    a,b = map(int, input().split())
    board[a-1][b-1] = 1
ans = 4
dfs(0,0,0)
print(ans if ans < 4 else -1)

