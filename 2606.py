"""
Method 1
"""

n,e = 7,6
l=[[],[2,5],[1,3,5],[2],[7],[1,2,6],[5],[4]]

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
e = int(input())

l=[[] for _ in range(n+1)]

for i in range(e):
    a,b = map(int, input().split())
    l[a].append(b)
    l[b].append(a)

visit = [False]*(n+1)

def bfs(v):
    queue = deque([v])
    visit[v] = True

    while queue:
        t = queue.popleft()

        for i in l[t]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True

bfs(1)
print(sum(visit)-1)

"""
Method 2
"""

import sys
input = sys.stdin.readline
n = int(input())
e = int(input())

l=[[] for _ in range(n+1)]

for i in range(e):
    a,b = map(int, input().split())
    l[a].append(b)
    l[b].append(a)

visit = [False]*(n+1)

def dfs(v):
    visit[v] = True
    for i in l[v]:
        if not visit[i]:
            dfs(i)

dfs(1)
print(sum(visit)-1)