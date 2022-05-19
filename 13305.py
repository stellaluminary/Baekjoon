n=7
a=[2,3,1,3,3,1]
b=[5,2,4,1,3,2,1]

"""
Method 1
"""
# import sys
# input=sys.stdin.readline
# n=int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# min_v=b[0]
# s=0
# for i in range(n-1):
#     if b[i] == 1:
#         s += sum(a[i:])
#         break
#     if b[i] < min_v:
#         min_v = b[i]
#     s += a[i]*min_v
# print(s)

"""
Method 2
"""
import sys
input=sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s, m = 0, b[0]
for i,j in zip(a,b[:-1]):
    if j < m:
        m = j
    s += i*m
print(s)