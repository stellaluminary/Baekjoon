"""
Method 1
시간 초과
"""

# import sys
# input = sys.stdin.readline
# n=int(input())
# l = list(map(int, input().split()))
#
# ans = []
# for i in range(n):
#     s = []
#     flg = 0
#     for j in range(i+1,n):
#         s.append(l[j])
#         if l[j] > l[i]:
#             ans.append(s.pop())
#             flg = 1
#             break
#     if flg == 0:
#         ans.append(-1)
#
# for i in ans:
#     print(i, end=' ')

"""
Method 2
"""
n=4
# l=[3,5,2,7]
l=[9,5,4,8]

import sys
input = sys.stdin.readline

#n = int(input())
#l = list(map(int, input().split()))

NGE = [-1] * n
stack = []

for i in range(n):
    while stack and l[stack[-1]] < l[i]:
        NGE[stack.pop()] = l[i]
    stack.append(i)
    print(stack, NGE)

print(*NGE)