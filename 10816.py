"""
Method 1
"""
# n = int(input())
# a = sorted(list(map(int, input().split())))
# m = int(input())
# b = list(map(int, input().split()))
#
# def bs(l, target, start, end):
#     if start > end:
#         return 0
#     mid = (start + end) // 2
#     if l[mid] == target:
#         return cnt.get(target)
#     elif l[mid] > target:
#         return bs(l, target, start, mid-1)
#     else:
#         return bs(l, target, mid+1, end)
#
# # n=10
# # a=sorted([6,3,2,10,10,10,-10,-10,7,3])
# # m=8
# # b=[10,9,-5,2,3,4,5,-10]
#
# cnt = {}
# for i in a:
#     if i in cnt:
#         cnt[i] += 1
#     else:
#         cnt[i] = 1
#
# for i in b:
#     print(bs(a, i, 0, len(a)-1), end=' ')

"""
Method 2
"""

n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = list(map(int, input().split()))

# n=10
# a=sorted([6,3,2,10,10,10,-10,-10,7,3])
# m=8
# b=[10,9,-5,2,3,4,5,-10]

cnt = {}
for i in a:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in b:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')