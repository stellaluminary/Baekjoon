"""
Method 1

"""

from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int, input().split())
q = deque()
for i in range(1,n+1):
    q.append(i)

print('<', end='')
while q:
    for i in range(k-1):
        q.append(q.popleft())
    n = q.popleft()
    if q:
        print(n, end=', ')
    else:
        print(n, end='>')









