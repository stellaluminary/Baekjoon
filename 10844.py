"""
Method 1
"""

n = int(input())
D = [[0]*10 for _ in range(n+1)]
D[1]=[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2,n+1):
    D[i][0] = D[i - 1][1]
    D[i][9] = D[i - 1][8]
    for j in range(1,9):
        D[i][j] = D[i-1][j-1] + D[i-1][j+1]
print(sum(D[n])%1000000000)



# n=int(input())
#
# l=[]
# ck = 0
# b = True
# for i in range(10**(n-1), 10**n):
#     t = i
#     for j in range(n):
#         l.append(t%10)
#         t = t//10
#
#     if len(l) == 1:
#         ck += 1
#
#     for j in range(len(l)-1):
#         if abs(l[j]-l[j+1]) == 1 and b == True:
#             if j == len(l)-2:
#                 ck += 1
#             b = True
#         else:
#             b = False
#             break
#     b = True
#     l = []
#
# print(ck)