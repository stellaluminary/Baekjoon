"""
Method 1
"""

# import sys
# input = sys.stdin.readline
# n=int(input())
# l=[0]+[int(input()) for _ in range(n)]
# d=[0]*(n+1)
# d[1] = l[1]
# if n>1:
#     d[2] = l[1]+l[2]
# for i in range(3,len(d)):
#     d[i] = max(l[i]+d[i-2], l[i]+l[i-1]+d[i-3], d[i-1])
# print(d)
# print(max(d))

# d[i-1] 없을 때 : [0, 6, 16, 23, 28, 33, 32, 34, 36, 38]
# d[i-1] 있을 때 : [0, 6, 16, 23, 28, 33, 33, 34, 36, 39]

"""
Method 2
"""
import sys
input = sys.stdin.readline
l=[int(input()) for _ in range(int(input()))]
d=[0,l[0],0]
for i in l[1:]:
    d=[max(d),d[0]+i,d[1]+i]
print(max(d))















