"""
Method 3

"""

"""
Method 2

"""
n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = []
left, right = 0, n-1
d = 1e10
while left < right:
    lv = l[left]
    rv = l[right]
    diff = lv + rv
    if abs(diff) < d:
        d = abs(diff)
        ans = (lv, rv)
    if diff < 0:
        left += 1
    else:
        right -= 1
print(*ans)

"""
Method 1
시간 초과
"""
n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = []
d = 1e10
for i in range(n-1):
    for j in range(i+1, n):
        diff = abs(l[i] + l[j])
        if diff < d:
            d = diff
            ans = (l[i], l[j])
print(*ans)
