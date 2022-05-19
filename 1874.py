"""
Method 1
"""

#n=8
#l=[4,3,6,8,7,5,2,1]

# n=5
# l=[1,2,5,3,4]


# stack = []
# ans = []
# flg = 0
# cnt = 0
#
# for i in range(int(input())):
#     num = int(input())
#
#     while cnt < num:
#         cnt += 1
#         stack.append(cnt)
#         ans.append('+')
#
#     if stack[-1] == num:
#         stack.pop()
#         ans.append('-')
#     else:
#         print('NO')
#         flg = 1
#         break
#
# if flg == 0:
#     for i in ans:
#         print(i)

"""
Method 2
"""

import sys
input = sys.stdin.readline

n = int(input())
targets = [int(input()) for _ in range(n)]
current = 1
stack, answer = [], []

for target in targets:
    while current <= target:
        stack.append(current)
        answer.append('+')
        current += 1

    if stack[-1] == target:
        answer.append('-')
        stack.pop()
    else:
        answer = ['NO']
        break

print('\n'.join(answer))