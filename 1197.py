"""
Method 1

MST 최소 신장 트리
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

v, e = map(int, input().split())
edges=[]
for i in range(e):
    a, b, c = map(int, input().split())
    edges.append((c,a,b))
edges.sort()

p = [i for i in range(v+1)]
res = 0
for edge in edges:
    c, a, b = edge
    if f_p(p, a) != f_p(p, b):
        union(p, a, b)
        res += c
print(res)


"""
Method 2

"""






"""
Method 3

"""