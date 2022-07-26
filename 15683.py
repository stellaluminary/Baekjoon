"""
Method 1

"""
import copy

n,m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
mode = [
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    [[0,1,2,3]]
]
cctv = []
ans = 1e9

for i in range(n):
    for j in range(m):
        if office[i][j] in [1,2,3,4,5]:
            cctv.append([office[i][j],i,j])

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def move(board, cctv_dir, x, y):
    for i in cctv_dir:
        nx, ny = x,y
        while 1:
            nx, ny = nx + dx[i], ny + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or board[nx][ny]==6:
                break
            if board[nx][ny] == 0:
                board[nx][ny] = 7

def dfs(depth, arr):
    global ans

    if depth == len(cctv):
        zero = 0
        for i in range(n):
            zero += arr[i].count(0)
        ans = min(ans, zero)
        return

    cctv_n, x, y = cctv[depth]
    for i in mode[cctv_n]:
        tmp = copy.deepcopy(arr)
        move(tmp, i, x, y)
        dfs(depth+1, tmp)


dfs(0, office)
print(ans)


























# def move(x,y,dir):
#     tmp = []
#     if 0 in dir:
#         for i in range(x-1, -1, -1):
#             if office[i][y] != 6:
#                 tmp.append((i,y))
#             else:
#                 break
#     if 1 in dir:
#         for j in range(y+1, m):
#             if office[x][j] != 6:
#                 tmp.append((x,j))
#             else:
#                 break
#     if 2 in dir:
#         for i in range(x+1, n):
#             if office[i][y] != 6:
#                 tmp.append((i,y))
#             else:
#                 break
#     if 3 in dir:
#         for j in range(y-1, -1, -1):
#             if office[x][j] != 6:
#                 tmp.append((x,j))
#             else:
#                 break
#     return tmp




















