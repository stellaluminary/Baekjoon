"""
Method 1

"""
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(i, j, country):
    if i <= -1 or i >= len(arr) or j <= -1 or j >= len(arr[0]):
        return 0
    if visit[i][j] == 0 and arr[i][j]:
        visit[i][j] = country
        ctry_coord.append((i,j,country))
        for k in range(4):
            nx, ny = i+dx[k], j+dy[k]
            dfs(nx, ny, country)
    return 0

def distance():
    for coord in ctry_coord:
        i, j, country_num = coord
        for k in range(4):
            dist=0
            nx, ny = i + dx[k], j + dy[k]

            while True:
                if nx <= -1 or nx >= len(visit) or ny <= -1 or ny >= len(visit[0]):
                    break
                else:
                    if country_num == visit[nx][ny]:
                        break

                    if visit[nx][ny] == 0:
                        nx, ny = nx + dx[k], ny + dy[k]
                        dist += 1
                        continue

                    if dist < 2:
                        break

                    edges.append((dist, country_num, visit[nx][ny]))
                    break

def f_p(p, x):
    if p[x] != x:
        p[x] = f_p(p, p[x])
    return p[x]

def union(p, a, b):
    a, b = f_p(p, a), f_p(p, b)
    p[max(a,b)] = min(a,b)

n,m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

visit = [[0]*m for i in range(n)]
country = 0
ctry_coord = []
edges = []
res = 0

for i in range(n):
    for j in range(m):
        if not visit[i][j] and arr[i][j] == 1:
            country += 1
            dfs(i, j, country)

p = [i for i in range(country+1)]

distance()
edges.sort()
cnt = 0
for edge in edges:
    c, a, b = edge

    if f_p(p, a) != f_p(p, b):
        union(p, a, b)
        res += c
        cnt += 1

if cnt == country-1:
    print(res)
else:
    print(-1)




