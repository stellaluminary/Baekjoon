"""
Method 1
"""
# n=int(input())
# l=list(map(int, input().split()))
# d1=[1]*n
# d2=[1]*n
# for i in range(1,n):
#     for j in range(i):
#         if l[i] > l[j]:
#             d1[i]=max(d1[i], d1[j]+1)
#         if l[n-1-i] > l[n-1-j]:
#             d2[n-1-i] = max(d2[n-1-i], d2[n-1-j]+1)
#
# for i in range(n):
#     d1[i]=d1[i]+d2[i]
# print(max(d1)-1)

# d1 : [1, 2, 2, 1, 3, 3, 4, 5, 2, 1]
# d2 : [1, 5, 2, 1, 4, 3, 3, 3, 2, 1]

"""
Method 2
"""
n=int(input())
l=list(map(int, input().split()))
d1=[1]*n
d2=[1]*n
for i in range(n):
    for j in range(i):
        if l[i] > l[j] and d1[i] <= d1[j]:
            d1[i]=d1[j]+1

for i in range(n-1,-1,-1):
    for j in range(i,n):
        if l[i] > l[j] and d2[i] <= d2[j]:
            d2[i] = d2[j] + 1

for i in range(n):
    d1[i]=d1[i]+d2[i]-1
print(max(d1))



