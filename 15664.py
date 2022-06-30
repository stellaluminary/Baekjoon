"""
Method 3

"""

"""
Method 2

"""


"""
Method 1

"""

def dfs(idx):
    global n, m
    if idx == m:
        print(*s)
        return

    overlap = 0
    for i in range(n):
        if not visit[i] and overlap != l[i] and (len(s) == 0 or s[-1] <= l[i]):
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
visit = [0]*n
s = []
dfs(0)