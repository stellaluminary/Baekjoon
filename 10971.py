"""
Method 2

"""

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
visit = [0] * n
m = 1e9

def dfs(depth, start, cost):
    global m
    if depth == n-1 and l[start][0] != 0:
        m = min(m, cost+l[start][0])
        return
    for i in range(n):
        if not visit[i] and l[start][i] != 0:
            visit[i] = 1
            dfs(depth+1, i, cost+l[start][i])
            visit[i] = 0
visit[0] = 1
dfs(0, 0, 0)
print(m)

"""
Method 1

"""

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
t = []
visit = [0] * n
m = 1e9

def dfs(depth, start, init):
    global m
    if depth == n and l[start][init] != 0:
        m = min(m, sum(t)+l[start][init])
        return
    for i in range(n):
        if not visit[i] and l[start][i] != 0:
            visit[i] = 1
            t.append(l[start][i])
            dfs(depth+1, i, init)
            t.pop()
            visit[i] = 0

for i in range(n):
    visit[i] = 1
    dfs(1, i, i)
    visit[i] = 0
print(m)







