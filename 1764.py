"""
Method 4

"""

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
d = [input().rstrip() for _ in range(n)]
b = [input().rstrip() for _ in range(m)]

res = sorted(list(set(d) & set(b)))

print(len(res))
print('\n'.join(res))

"""
Method 3

"""

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
a,b = set(), set()

for i in range(n):
    a.add(input().rstrip())

for i in range(m):
    b.add(input().rstrip())

res = sorted(list(a & b))

print(len(res))
print('\n'.join(res))




"""
Method 2

"""
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
c = {}
l = []
cnt = 0

for i in range(n):
    c[input().rstrip()] = 1

for j in range(m):
    t = input().rstrip()
    if t in c:
        cnt += 1
        l.append(t)

l.sort()
print(cnt)
print('\n'.join(l))

"""
Method 1
시간 초과
"""
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
d = [input().rstrip() for _ in range(n)]
b = [input().rstrip() for _ in range(m)]
d.sort()
l = []
cnt = 0
for i in d:
    if i in b:
        cnt += 1
        l.append(i)





