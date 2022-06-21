"""
Method 1

최소 신장 트리 - 크루스칼 알고리즘
"""


import sys
input = sys.stdin.readline

def f_p(p, x):
    if p[x] != x:
        p[x] = f_p(p, p[x])
    return p[x]

def union(p, a, b):
    a = f_p(p, a)
    b = f_p(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

t = int(input())
for i in range(t):
    n, m = map(int, input().split())

    p = [j for j in range(n+1)]
    res = 0

    for e in range(m):
        a,b = map(int, input().split())
        if f_p(p, a) != f_p(p, b):
            union(p, a, b)
            res += 1

    print(res)


"""
Method 2

신장 트리의 특성 상 노드-1의 값이 정답
"""


import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    for e in range(m):
        a,b = map(int, input().split())
    print(n-1)



"""
Method 3

"""

import sys
input = sys.stdin.readline

def dfs(idx, cnt):
    visit[idx] = 1
    for i in graph[idx]:
        if visit[i] == 0:
            cnt = dfs(i, cnt+1)
    return cnt

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    visit = [0]*(n+1)
    cnt = dfs(1, 0)
    print(cnt)


