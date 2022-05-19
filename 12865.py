# import sys
# input=sys.stdin.readline
# # n,k=map(int, input().split())
# # l=[list(map(int, input().split())) for _ in range(n)]
# n,k = 6,7
# l=[[6,13],[4,8],[3,6],[5,12],[1,5],[2,4]]
# d=[[0]*(k+1) for _ in range(n)]
# print(len(d), len(d[0]), d)
# for i in range(n):
#     w = l[i][0]
#     v = l[i][1]
#     print(i, w, v)
#     for j in range(1,k+1):
#         if j < w:
#             d[i][j] = d[i-1][j]
#         else:
#             d[i][j] = max(d[i - 1][j-w]+v, d[i-1][j])
#         print(j, w, j-w, d[i - 1][j-w]+v, d[i-1][j], d[i])
#     print(d)
#
#
# print(d)
# print(d[-1][k])
"""
Method 2
"""
import sys
input=sys.stdin.readline
n,k=map(int, input().split())
l=[list(map(int, input().split())) for _ in range(n)]
l.sort()
d=[0]*(k+1)
for w,v in l:
    for i in range(k,w-1,-1):
        d[i] = max(d[i-w]+v, d[i])
print(d[k])

"""
Method 1
"""
import sys
input=sys.stdin.readline
n,k=map(int, input().split())
l=[list(map(int, input().split())) for _ in range(n)]
d=[[0]*(k+1) for _ in range(n)]
for i in range(n):
    w = l[i][0]
    v = l[i][1]
    for j in range(1,k+1):
        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i - 1][j-w]+v, d[i-1][j])
print(d[-1][k])