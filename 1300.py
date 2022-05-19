# n,k = 3,7

n = int(input())
k = int(input())
start, end = 1, k

while start <= end:
    mid = (start+end)//2
    cnt = 0

    for i in range(1, n+1):
        cnt += min(mid//i, n)
    print(start, end, mid, cnt)
    if cnt >= k:
        end = mid - 1
    else:
        start = mid + 1
print(start)

"""
Memory 초과
너무 많은 값들을 저장하고 sorted하는 것은 무리
"""
# n=int(input())
# k=int(input())
#
# b=[]
# for i in range(n):
#     for j in range(n):
#         b.append((i+1)*(j+1))
#
# b = sorted(b)
# print(b[k])