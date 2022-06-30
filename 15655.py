"""
Method 1

"""

def dfs(idx):
    global n, m
    if idx == m:
        print(*s)
        return

    for i in l:
        if len(s)==0 or s[-1] < i and i not in s:
            s.append(i)
            dfs(idx+1)
            s.pop()

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
s = []
dfs(0)