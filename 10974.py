"""
Method 2

"""

n = int(input())
s = [i for i in range(1,n+1)]
t = []
def dfs(depth):
    if depth == n:
        print(*t)
        return

    for i in range(n):
        if s[i] not in t:
            t.append(s[i])
            dfs(depth+1)
            t.pop()

dfs(0)

"""
Method 1
"""
from itertools import permutations
n = int(input())
for i in permutations([s for s in range(1,n+1)]):
    print(*i)
