"""
Method 3

"""

"""
Method 2

"""

from collections import deque

n = int(input())
k = int(input())
arr = [[0]*n for _ in range(n)]
for _ in range(k):
    a,b = map(int, input().split())
    arr[a-1][b-1] = 2

l = int(input())
times = {}
for _ in range(l):
    a, b = input().split()
    times[int(a)] = b

# east, south, west, north
dx = [0,1,0,-1]
dy = [1,0,-1,0]

q = deque()
x, y = 0, 0
q.append((x,y))
arr[x][y] = 1
time, d = 0, 0

while 1:
    time += 1
    x, y = x + dx[d], y + dy[d]

    if 0 <= x < n and 0 <= y < n and arr[x][y] != 1:
        # not visit & not my body
        if arr[x][y] == 0:
            tx, ty = q.popleft()
            arr[tx][ty] = 0
        arr[x][y] = 1
        q.append((x, y))
    # touch my body
    else:
        break

    if time in times:
        if times[time] == 'L':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4

print(time)

"""
Method 1

"""

from collections import deque

n = int(input())
k = int(input())
arr = [[0]*n for _ in range(n)]
for _ in range(k):
    a,b = map(int, input().split())
    arr[a-1][b-1] = 2

l = int(input())
times = {}
for _ in range(l):
    a, b = input().split()
    times[int(a)] = b

def turn(char):
    global current_dir
    if char == 'L':
        current_dir = (current_dir - 1) % 4
    else:
        current_dir = (current_dir + 1) % 4

# east, south, west, north
dx = [0,1,0,-1]
dy = [1,0,-1,0]

q = deque()
q.append((0,0))
x, y = 0, 0
arr[x][y] = 1
time, current_dir = 0, 0

while 1:
    time += 1
    x, y = x + dx[current_dir], y + dy[current_dir]

    if x < 0 or y < 0 or x >= n or y >= n:
        break

    # eat apple
    if arr[x][y] == 2:
        arr[x][y] = 1
        q.append((x,y))
        if time in times:
            turn(times[time])
    # not visit & not my body
    elif arr[x][y] == 0:
        arr[x][y] = 1
        q.append((x,y))
        tx, ty = q.popleft()
        arr[tx][ty] = 0
        if time in times:
            turn(times[time])
    # touch my body
    else:
        break

print(time)

























