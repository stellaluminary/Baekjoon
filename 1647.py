"""
Method 1

"""

"""
n,m=7,12
edges = [(1, 3, 2), (1, 6, 4), (2, 1, 3), (2, 1, 6), (2, 2, 5), (3, 1, 2), (3, 4, 5), (3, 6, 5), (4, 3, 4), (4, 6, 7), (5, 5, 1), (6, 7, 3)]
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

n,m = map(int, input().split())

p = [0] * (n+1)
for i in range(n+1):
    p[i] = i

edges = []
for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

res = 0
last = 0
for edge in edges:
    c, a, b = edge
    if f_p(p, a) != f_p(p, b):
        union(p, a, b)
        res += c
        last = c

print(res - last)
