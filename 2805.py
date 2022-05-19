"""
Method 1
"""
# n, m = 4,7
# l = sorted([20,15,10,17])
#
# n, m = 5, 20
# l = sorted([4, 42, 40, 26, 46])
import sys
input = sys.stdin.readline

# n, m = map(int, input().split())
# l = list(map(int, input().split()))
n, m = 5, 20
l = sorted([4, 42, 40, 26, 46])
start, end = 1, max(l)

while start <= end:
    mid = (start+end)//2

    cl = sum(i-mid if i>mid else 0 for i in l)

    if cl >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)


