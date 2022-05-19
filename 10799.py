"""
Method 1
시간 초과
"""

"""
t = [i for i in input()]

stack = []
loc = []
laser = []

for i in range(len(t)):
    if t[i] == '(':
        stack.append(i)
    if t[i] == ')':
        tmp = stack.pop()

        if i - tmp == 1:
            laser.append(tmp)
        else:
            loc.append([tmp, i])

cnt = 0
for s,e in loc:
    las = 0
    for j in laser:
        if s < j < e:
            las += 1

    cnt += las + 1
print(cnt)
"""

"""
Method 2
"""

"""
t = [i for i in input()]
stack = []
cnt = 0
stick_cnt = 0
for i in range(len(t)):
    if t[i] == '(':
        stack.append(i)
    if t[i] == ')':
        tmp = stack.pop()
        if i - tmp == 1:
            cnt += len(stack)
        else:
            stick_cnt += 1
print(cnt+stick_cnt)
"""
"""
Method 3
"""

import sys
t = [i for i in sys.stdin.readline().rstrip()]
stack = []
cnt = 0
for i in range(len(t)):
    if t[i] == '(':
        stack.append(i)
    else:
        tmp = stack.pop()
        if t[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)
