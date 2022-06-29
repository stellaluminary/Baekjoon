"""
Method 1

"""

n, m = list(map(int, input().split()))
s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
dfs()

"""
Method 2
"""

def dfs(step):
    if step == m:
        print(' '.join(t))
        return

    for i in range(1, n+1):
        if not visit[i]:
            visit[i] = 1
            t.append(str(i))
            dfs(step+1)
            visit[i] = 0
            t.pop()

import sys
input = sys.stdin.readline
n,m = map(int, input().split())

visit = [0] * (n+1)
t = []
dfs(0)

"""
Method 3
"""

import itertools

n, m = map(int, input().split())
t = list(itertools.permutations([i for i in range(1, n+1)], m))
for i in t:
    print(' '.join(map(str, i)))

"""
Method 4
"""

from itertools import permutations

N, M = map(int, input().split())
li = map(str, range(1, N+1))
print('\n'.join(list(map(' '.join,permutations(li, M)))))