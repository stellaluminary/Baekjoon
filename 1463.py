"""
Method 1
"""
# x = int(input())
# dp = [0 for _ in range(x+1)]
# dp[1] = 0
# for i in range(2, x+1):
#     dp[i] = dp[i-1] + 1
#     if not i % 2 and dp[i] > dp[i//2] + 1:
#         dp[i] = dp[i//2] + 1
#     if not i % 3 and dp[i] > dp[i//3] + 1:
#         dp[i] = dp[i//3] + 1
#
# print(dp[x])

"""
Method 2
"""

# x = int(input())
# dp = [0 for _ in range(x+1)]
# for i in range(2, x+1):
#     dp[i] = dp[i-1] + 1
#     if i % 3 == 0:
#         dp[i] = min(dp[i], dp[i//3] + 1)
#     if i % 2 == 0:
#         dp[i] = min(dp[i], dp[i//2] + 1)
#
# print(dp[x])


"""
Method 3
"""
n = int(input())
r = {1:0, 2:1}
def bfs(n):
    if n in r:
        return r[n]
    m = min(bfs(n//2)+n%2, bfs(n//3)+n%3) + 1
    r[n] = m
    return m

print(bfs(n))


# n = int(input())
# l = [[0]*3 for _ in range(n//2+1)]
# l[0] = [n,n,n]
#
# for i in range(n//2):
#     for j in range(3):
#         if l[i][j] == 0:
#             continue
#         if l[i][j] % 3 == 0:
#             if l[i+1][0] == 0:
#                 l[i+1][0] = l[i][j] // 3
#             elif l[i+1][0] != 0:
#                 l[i + 1][0] = min(l[i][j] // 3, l[i+1][0])
#
#         if l[i][j] % 2 == 0:
#             if l[i+1][1] == 0:
#                 l[i+1][1] = l[i][j] // 2
#             elif l[i+1][1] != 0:
#                 l[i + 1][1] = min(l[i][j] // 2, l[i+1][1])
#
#         if l[i][j] -1 >0:
#             if l[i + 1][2] == 0:
#                 l[i + 1][2] = l[i][j] - 1
#             elif l[i + 1][2] != 0:
#                 l[i + 1][2] = min(l[i][j] -1, l[i + 1][2])
#     if 1 in l[i+1]:
#         break
#
# print(i+1)