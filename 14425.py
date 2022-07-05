"""
Method 3

"""

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
s = set([input().rstrip() for _ in range(n)])
cnt = 0

for _ in range(m):
    t = input().rstrip()
    if t in s:
        cnt += 1

print(cnt)

"""
Method 2

"""
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
d = dict()
cnt = 0
for _ in range(n):
    s = input().rstrip()
    d[s] = 1

for i in range(m):
    t = input().rstrip()
    if t in d:
        cnt += 1

print(cnt)

"""
Method 1

"""

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
ns = [input().rstrip() for _ in range(n)]

cnt = 0
for i in range(m):
    t = input().rstrip()
    if t in ns:
        cnt += 1

print(cnt)