n=7
l=[10, 20, 40, 30, 60, 25, 80]

"""
Method 1
"""
from bisect import bisect_left

n=int(input())
l=list(map(int, input().split()))
d = [0]

for i in l:
    if d[-1] < i:
        d.append(i)
    else:
        d[bisect_left(d, i)] = i

print(len(d)-1)

"""
Method 1
"""

# n=int(input())
# l=list(map(int, input().split()))
d = [l[0]]

def bs(target, start, end):
    while start <= end:
        mid = (start + end)//2
        if d[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return start

for i in l:
    if d[-1] < i:
        d.append(i)
    else:
        d[bs(i, 0, len(d)-1)] = i

print(len(d))

"""
Method 1
시간 초과
https://www.acmicpc.net/problem/11722
다이나믹 프로그래밍
"""
# d = [1]*n
#
# max_v = l[0]
# for i in range(1, n):
#     for j in range(i):
#         if l[i]>l[j]:
#             d[i] = max(d[i], d[j]+1)
# print(d)





