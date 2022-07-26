"""
Method 2

"""
from collections import Counter
n = int(input())
arr = list(map(int, input().split()))
b,c = map(int,input().split())
cnt = 0

counts = Counter(arr)
for k, v in counts.items():
    p = 1
    k -= b
    if k > 0:
        div, mod = divmod(k, c)
        p += div
        if mod > 0:
            p += 1
    cnt += p*v

print(cnt)

"""
Method 1

"""
import math
n = int(input())
arr = list(map(int, input().split()))
b,c = map(int,input().split())
cnt = 0
for a in arr:
    if a - b > 0:
        cnt += 1 + math.ceil((a-b)/c)
    else:
        cnt += 1
print(cnt)