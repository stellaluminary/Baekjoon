"""
Method 2

"""
n = int(input())
s = list(map(int, input().split()))
s.sort()
m = int(input())
r = list(map(int, input().split()))

def binary_search(start,end,target):
    while start <= end:
        mid = (start+end)//2
        if s[mid] == target:
            return 1
        elif s[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for i in r:
    print(binary_search(0, n-1, i), end=' ')

"""
Method 1

"""

n = int(input())
s = list(map(int, input().split()))
m = int(input())
r = list(map(int, input().split()))

for i in r:
    if i in s:
        print(1, end=' ')
    else:
        print(0, end=' ')





