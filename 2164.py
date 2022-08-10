
"""
Method 2

"""
a,b = int(input()), 1
while a>b:
    b*=2
print(a*2-b)

"""
Method 1

"""

from collections import deque
c = deque([i for i in range(1, int(input()) + 1)])
while len(c) != 1:
    t = c.popleft()
    c.append(c.popleft())
print(c.popleft())