"""
Method 2

"""
import copy
import sys
input = sys.stdin.readline

r,c,t = map(int, input().split())
room = []
condition = []

for i in range(r):
    tmp = list(map(int, input().split()))
    room.append(tmp)
    if tmp[0] == -1:
        condition.append(i)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def diffusion():
    tmp = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if room[i][j] == -1:
                tmp[i][j] = -1
            elif room[i][j]:
                cnt = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if nx <0 or ny < 0 or nx >= r or ny >= c:
                        continue
                    if room[nx][ny] == -1:
                        continue
                    cnt += 1
                    tmp[nx][ny] += room[i][j] // 5
                tmp[i][j] += room[i][j] - (room[i][j] // 5)*cnt
    return tmp

def acting(x, dir):
    tmp = copy.deepcopy(room)
    cx, cy = x, 0
    room[x][1] = 0
    y = 1
    for i in range(4):
        while 1:
            nx, ny = x + dx[dir[i]], y + dy[dir[i]]
            if nx == cx and ny == cy:
                return
            if 0 <= nx < r and 0 <= ny < c:
                room[nx][ny] = tmp[x][y]
            else:
                break
            x, y = nx, ny

for i in range(t):
    room = diffusion()
    acting(condition[0], [3,0,2,1])
    acting(condition[1], [3,1,2,0])

print(sum(map(sum, room))+2)

"""
Method 1

"""

r,c,t = map(int, input().split())
room = []
condition = []
for i in range(r):
    tmp = list(map(int, input().split()))
    room.append(tmp)
    if tmp[0] == -1:
        condition.append(i)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def diffusion():
    tmp = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if room[i][j] == -1:
                tmp[i][j] = -1
            elif room[i][j]:
                cnt = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if nx <0 or ny < 0 or nx >= r or ny >= c:
                        continue
                    if room[nx][ny] == -1:
                        continue
                    cnt += 1
                    tmp[nx][ny] += room[i][j] // 5
                tmp[i][j] += room[i][j] - (room[i][j] // 5)*cnt
    return tmp

def acting():
    tmp = [[0]*c for _ in range(r)]
    for i in range(r):
        if i == 0:
            tmp[i][:-1] = room[i][1:]
            tmp[i][-1] = room[i+1][-1]
        elif i == r-1:
            tmp[i][:-1] = room[i][1:]
            tmp[i][-1] = room[i - 1][-1]
        elif i < condition[0]:
            tmp[i][0] = room[i-1][0]
            tmp[i][-1] = room[i + 1][-1]
            tmp[i][1:-1] = room[i][1:-1]
        elif i == condition[0] or i == condition[1]:
            tmp[i][2:] = room[i][1:-1]
        elif i > condition[1]:
            tmp[i][0] = room[i + 1][0]
            tmp[i][-1] = room[i - 1][-1]
            tmp[i][1:-1] = room[i][1:-1]

    tmp[condition[0]][0], tmp[condition[1]][0] = -1, -1
    return tmp

for i in range(t):
    room = diffusion()
    room = acting()

print(sum(map(sum, room))+2)
