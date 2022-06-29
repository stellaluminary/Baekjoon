"""
Method 3

"""

"""
Method 2

"""

from itertools import product
n,m = map(int, input().split())
for x in product(range(1, n+1), repeat=m):
    print(*x)

"""
Method 1

"""

def dfs():
    if len(t) == m:
        print(' '.join(map(str, t)))
        return

    for i in range(1, n+1):
        t.append(i)
        dfs()
        t.pop()

n,m = map(int, input().split())
t = []
dfs()





