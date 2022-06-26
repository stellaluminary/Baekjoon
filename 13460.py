"""
Method 1

"""

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l=[]
for i in range(n):
    l.append(list(input().rstrip()))
    for j in range(m):
        if l[i][j] == 'R':
            rx, ry = i,j
        elif l[i][j] == 'B':
            bx, by = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visit = [[[[False] * m for i in range(n)] for i in range(m)] for i in range(n)]

def move(i, j, dx, dy):
    c = 0
    while l[i+dx][j+dy] != '#' and l[i][j] != 'O':
        i += dx
        j += dy
        c += 1
    return i, j, c

def bfs(rx, ry, bx, by, d):
    q = deque()
    q.append([rx,ry,bx,by, d])
    visit[rx][ry][bx][by] = True

    while q:
        rx, ry, bx, by, d = q.popleft()
        if d > 10:
            break
        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i])
            nbx, nby, bc = move(bx, by, dx[i], dy[i])
            if l[nbx][nby] != 'O':
                if l[nrx][nry] == 'O':
                    print(d)
                    return
                if nrx == nbx and nry == nby:
                    if rc > bc:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if not visit[nrx][nry][nbx][nby]:
                    visit[nrx][nry][nbx][nby] = True
                    q.append([nrx, nry, nbx, nby, d+1])
                    print(q)
    print(-1)

bfs(rx, ry, bx, by, 1)







"""
Method 2

"""

