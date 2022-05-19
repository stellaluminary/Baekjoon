# n=5
# a=[4,1,5,2,3]
# m=5
# b=[1,3,7,9,5]

"""
Method 1
"""

import sys
input=sys.stdin.readline

def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if arr[mid] == target:
        return target
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)

n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int, input().split()))
a.sort()
for i in range(m):
    if binary_search(a, b[i], 0, n-1):
        print(1)
    else:
        print(0)

"""
Method 2
"""

import sys
input=sys.stdin.readline
input()
a=set(input().split())
input()
for i in input().split():
    print(1) if i in a else print(0)