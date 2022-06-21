"""
Method 1


"""

import sys
import math

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

n = int(input())
p = [i for i in range(n+1)]

edges = []
coord = []
res = 0

for _ in range(n):
    x, y = map(float, input().split())
    coord.append((x,y))

for i in range(n-1):
    for j in range(i+1, n):
        edges.append((math.sqrt((coord[i][0] - coord[j][0])**2 + (coord[i][1] - coord[j][1])**2), i+1, j+1))

edges.sort()

for edge in edges:
    c, a, b = edge
    if f_p(p, a) != f_p(p, b):
        union(p, a, b)
        res += c

print(round(res, 2))


"""
Method 2

"""






"""
Method 3

"""