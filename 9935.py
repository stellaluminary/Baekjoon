"""
Method 2

"""
n = input()
m = input()

stack = []

for c in n:
    stack.append(c)
    if c == stack[-1] and ''.join(stack[-len(m):]) == m:
        del stack[-len(m):]

ans = ''.join(stack)
if ans == '':
    print('FRULA')
else:
    print(ans)

"""
Method 1

"""

import sys
input = sys.stdin.readline

n = input().rstrip()
m = input().rstrip()

while 1:
    n = n.replace(m, '')
    if m not in n:
        if len(n):
            print(n)
        else:
            print('FRULA')
        break