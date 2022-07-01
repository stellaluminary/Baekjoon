"""
Method 1

"""

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
r, c, d = map(int, input().split())
dir = [(-1,0), (0,1), (1,0), (0,-1)]
l = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def robot(x, y, d):
    global ans
    if not l[x][y]:
        l[x][y] = 2
        ans += 1

    for _ in range(4):
        nd = (d + 3) % 4
        nx, ny = x + dir[nd][0], y + dir[nd][1]
        if not l[nx][ny]:
            robot(nx, ny, nd)
            return
        d = nd

    nd = (d + 2) % 4
    nx, ny = x + dir[nd][0], y + dir[nd][1]
    if l[nx][ny] == 1:
        print(ans)
        exit(0)
    robot(nx, ny, d)

robot(r,c,d)