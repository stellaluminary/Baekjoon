"""
Method 1

5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19

메모리 문제 발생
"""

"""

import sys
input = sys.stdin.readline

def f_p(p,x):
    if p[x] != x:
        p[x] = f_p(p, p[x])
    return p[x]

def union(p,a,b):
    a, b = f_p(p,a), f_p(p,b)
    p[max(a,b)] = min(a,b)

def cost(c1, c2):
    return min(abs(c1[0]-c2[0]), abs(c1[1]-c2[1]), abs(c1[2]-c2[2]))

n = int(input())
p = [i for i in range(n+1)]
coord=[]
edges=[]
res=0

for _ in range(n):
    x,y,z = map(int, input().split())
    coord.append((x,y,z))

for i in range(n-1):
    for j in range(i+1, n):
        edges.append((cost(coord[i], coord[j]), i+1, j+1))

edges.sort()

for edge in edges:
    c, a, b = edge
    if f_p(p, a) != f_p(p, b):
        union(p, a, b)
        res += c

print(res)
"""


"""
Method 2

"""


import sys
input = sys.stdin.readline

def f_p(p,x):
    if p[x] != x:
        p[x] = f_p(p, p[x])
    return p[x]

def union(p,a,b):
    a, b = f_p(p,a), f_p(p,b)
    p[max(a,b)] = min(a,b)

n = int(input())
p = [i for i in range(n+1)]
coord=[]
edges=[]
res=0

for i in range(n):
    x,y,z = map(int, input().split())
    coord.append((x,y,z,i+1))

for i in range(3):
    coord.sort(key=lambda x:x[i])
    for j in range(1, n):
        edges.append((abs(coord[j-1][i] - coord[j][i]), coord[j-1][3], coord[j][3]))

edges.sort()

for edge in edges:
    c, a, b = edge
    if f_p(p, a) != f_p(p, b):
        union(p, a, b)
        res += c

print(res)




"""
Method 3

"""