"""
Method 2

"""

def dfs(idx):
    global n, m
    if idx == m:
        print(*s)
        return

    overlap = 0
    for i in range(n):
        if not visit[i] and overlap != l[i]:
            visit[i] = 1
            s.append(l[i])
            overlap = l[i]
            dfs(idx+1)
            visit[i] = 0
            s.pop()

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
l = sorted(list(map(int, input().split())))
visit=[0]*n
s = []

dfs(0)

"""
Method 1
시간 초과
"""

def dfs(idx):
    global m
    if idx == m:
        if s not in res:
            res.append(copy.deepcopy(s))
        return

    for i in l:
        if o[i] != 0:
            s.append(i)
            o[i] -= 1
            dfs(idx+1)
            s.pop()
            o[i] += 1

import sys
import copy
input = sys.stdin.readline

n,m = map(int, input().split())
l = sorted(list(map(int, input().split())))
s = []
o = {i:0 for i in l}
for i in range(len(l)):
    o[l[i]] += 1

res = []
dfs(0)
for i in res:
    print(*i)