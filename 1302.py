"""
Method 2

"""
import sys
input = sys.stdin.readline

n = int(input())
l = [input().rstrip() for _ in range(n)]
unique = []
for i in l:
    if i not in unique:
        unique.append(i)

num = sorted([(l.count(i),i) for i in unique], key=lambda x:(-x[0], x[1]))

print(num[0][1])



"""
Method 1

"""

import sys
input = sys.stdin.readline

n = int(input())
l = [input().rstrip() for _ in range(n)]
d = {}
for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

max_n = max(d.values())

res = []

for i in d:
    if d[i] == max_n:
        res.append(i)

print(sorted(res)[0])
