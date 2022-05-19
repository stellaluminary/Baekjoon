"""
Method 1
"""

# n=int(input())
# l=list(map(int,input().split()))
# d=[0]*n
# for i in range(n):
#     for j in range(i):
#         if l[i] > l[j] and d[i]<d[j]:
#             d[i] = d[j]
#     d[i] += 1
# print(max(d))

"""
Method 2
"""
n=int(input())
l=list(map(int,input().split()))
d=[1]*n
for i in range(n):
    for j in range(i):
        if l[i] > l[j]:
            d[i] = max(d[i], d[j]+1)
print(max(d))