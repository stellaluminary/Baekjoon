"""
Method 1

"""
from collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
    q = deque([s])
    visit[s]=True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visit[i]:
                visit[i] = True
                q.append(i)

n, m = map(int, input().split())
visit = [0]*(n+1)
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for i in range(1, n+1):
    if not visit[i]:
        bfs(i)
        cnt += 1

print(cnt)


"""
Method 2

"""

import sys
input = sys.stdin.readline

def f_p(p, x):
    if p[x] != x:
        p[x] = f_p(p, p[x])
    return p[x]

def union(p, a, b):
    a, b = f_p(p, a), f_p(p, b)
    p[max(a,b)] = min(a, b)

n, m = map(int, input().split())

p = [i for i in range(n+1)]
edges = []
for i in range(m):
    a, b = map(int, input().split())
    edges.append((a,b))

for edge in edges:
    a, b = edge
    union(p, a, b)

for i in range(1,n+1):
    p[i] = f_p(p, p[i])

print(len(set(p[1:])))

