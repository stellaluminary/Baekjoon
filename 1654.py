"""
Method 1
"""
k,n = 4,11
l = sorted([802,743,457,539])

# k, n = map(int, input().split())
# l = sorted([int(input()) for _ in range(k)])
# start, end = 1, l[-1]
# print(sum(l)//n)
# while start <= end:
#     mid = (start+end)//2
#     lines = 0
#     for i in l:
#         lines += i//mid
#     if lines >= n:
#         start = mid+1
#     else:
#         end = mid-1
# print(end)

"""
Method 2
"""
k,n = 4,11
l = sorted([802,743,457,539])

k, n = map(int, input().split())
l = sorted([int(input()) for _ in range(k)])
start, end = 1, sum(l)//n
while start <= end:
    mid = (start+end)//2
    lines = sum([i//mid for i in l])
    if lines >= n:
        start = mid+1
        ans = mid
    else:
        end = mid-1
print(ans)
