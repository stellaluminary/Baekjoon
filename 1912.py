"""
Method 1
"""
# n = int(input())
# #l = list(map(int, input().split()))
# l = [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]
# d=[l[0]]
# for i in range(1,n):
#     d.append(max(d[i-1]+l[i], l[i]))
# print(max(d))

"""
Method 2
"""
input()
a = list(map(int,input().split()))
if max(a) <= 0: print(max(a))
else:
    t = 0
    m = 0
    for i in a:
        t += i
        if t < 0:
            t = 0
        if m < t:
            m = t
    print(m)

"""
Method 3
시간초과
"""
# import sys
# input = sys.stdin.readline
# n = int(input())
# l = list(map(int, input().split()))
# d=[i for i in l]
#
# for i in range(n):
#     cnt = l[i]
#     for j in range(i-1,-1,-1):
#         cnt += l[j]
#         d[i] = max(d[i], cnt)
# print(max(d))