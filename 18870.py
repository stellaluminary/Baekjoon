"""
Method 2

"""

import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
s = sorted(set(l))
d = {s[i]:i for i in range(len(s))}
for i in l:
    print(d[i], end=' ')

"""
Method 1
시간 초과
"""

import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
s = sorted(set(l))
ans = []
for i in range(len(l)):
    ans.append(s.index(l[i]))
print(*ans)