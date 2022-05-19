# n, c= 5,3
# l = sorted([1,2,8,4,9])

n,c = map(int, input().split())
l = sorted([int(input()) for _ in range(n)])
start = 1
end = l[n - 1] - l[0]

while start <= end:
    cnt = 1
    mid = (start + end) // 2
    current = l[0]
    for x in l:
        if current + mid <= x:
            cnt += 1
            current = x
    if cnt >= c:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)

print(start, end, mid, cnt)