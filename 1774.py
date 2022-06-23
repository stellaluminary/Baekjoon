"""
Method 1

"""
import sys
input = sys.stdin.readline

def f_p(p, x):
    if p[x] != x:
        p[x] = f_p(p, p[x])
    return p[x]

def union(p, a, b):
    a, b = f_p(p, a), f_p(p, b)
    p[max(a,b)] = min(a,b)

def dist(c1, c2):
    return ((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)**0.5

n, m = map(int, input().split())

p = [i for i in range(n+1)]

coord, edges = [], []
res = 0

for i in range(n):
    x, y = map(int, input().split())
    coord.append((x,y))

for j in range(m):
    a, b = map(int, input().split())
    union(p, a, b)

for i in range(n-1):
    for j in range(i+1, n):
        edges.append((dist(coord[i], coord[j]), i+1, j+1))

edges.sort()

for edge in edges:
    c, a, b = edge
    if f_p(p, a) != f_p(p, b):
        union(p, a, b)
        res += c

print('%.2f' %(res))
