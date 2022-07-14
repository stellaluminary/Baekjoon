"""
Method 2

Python3 시간 초과
PyPy3 통과

"""

def check(t):
    res = 0
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if t[i][j-1] == t[i][j]:
                cnt += 1
            else:
                cnt = 1
            res = max(res, cnt)
        cnt = 1
        for j in range(1, n):
            if t[j-1][i] == t[j][i]:
                cnt += 1
            else:
                cnt = 1
            res = max(res, cnt)
    return res

n = int(input())
l = [list(input()) for _ in range(n)]
ans = 1

for i in range(n):
    for j in range(n):
        if j < n-1:
            l[i][j], l[i][j+1] = l[i][j+1], l[i][j]
            ans = max(ans, check(l))
            l[i][j], l[i][j+1] = l[i][j+1], l[i][j]

        if i < n-1:
            l[i][j], l[i+1][j] = l[i+1][j], l[i][j]
            ans = max(ans, check(l))
            l[i][j], l[i+1][j] = l[i+1][j], l[i][j]
print(ans)

"""
Method 1

시간 초과
"""

def check(t):
    global n
    res = 0

    # row
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if t[i][j-1] != t[i][j]:
                res = max(res, cnt)
                cnt = 1
            else:
                cnt += 1

            if j == n-1:
                res = max(res, cnt)

    # col
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if t[j-1][i] != t[j][i]:
                res = max(res, cnt)
                cnt = 1
            else:
                cnt += 1

            if j == n-1:
                res = max(res, cnt)
    return res

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def direction(x, y):

    cnt = 1
    for z in range(4):
        nx, ny = x+dx[z], y+dy[z]
        if nx<0 or nx >= n or ny < 0 or ny >= n:
            continue
        tmp_l = l[:]
        tmp_l[x][y], tmp_l[nx][ny] = tmp_l[nx][ny], tmp_l[x][y]
        cnt = max(cnt, check(tmp_l))

    return cnt


n = int(input())
l = [list(input()) for _ in range(n)]

ans = check(l)
for p in range(n):
    for q in range(n):
        ans = max(ans, direction(p, q))

print(ans)




