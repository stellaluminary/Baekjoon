"""
Method 1

"""
import sys

def dfs():
    if len(t) == m:
        print(' '.join(map(str, t)))
        return

    for i in range(1, n+1):
        if len(t) == 0 or t[-1] <= i:
            t.append(i)
            dfs()
            t.pop()

n,m = map(int, sys.stdin.readline().split())
t = []
dfs()



