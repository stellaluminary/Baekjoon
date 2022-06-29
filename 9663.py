"""
Method 5

"""

a = (0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596)
print(a[int(input())])

"""
Method 4

"""

N = int(input())
cnt = 0
bd = [False] * N  # idx는 j
diag1 = [False] * (2 * N)  # idx는 i+j
diag2 = [False] * (2 * N)  # idx는 i-j

# 다음 i번째 퀸을 j에 놓을 수 있는지 확인하는 함수.
def f(i):
    # 끝에 도달하면 종료
    if i == N:
        global cnt;
        cnt += 1
        return
    # 1. j값이 앞에랑 걸리는게 있는지?
    # 2. 대각선에 걸리는게 있는지?
    for j in range(N):
        if not (bd[j] or diag1[i + j] or diag2[i - j]):
            bd[j] = diag1[i + j] = diag2[i - j] = True
            f(i + 1)
            bd[j] = diag1[i + j] = diag2[i - j] = False

f(0)
print(cnt)

"""
Method 3

시간 초과
"""

import sys

def not_adj(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x-i:
            return False
    return True

def dfs(x):
    global res

    if x == n:
        res += 1
        return

    for i in range(n):
        if visit[i]:
            continue
        row[x] = i
        if not_adj(x):
            visit[i] = 1
            dfs(x+1)
            visit[i] = 0

n = int(sys.stdin.readline())
row = [0]*n
visit = [0]*n
res = 0
dfs(0)
print(res)


"""
Method 2

시간 초과
"""

def not_adj(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x-i:
            return False
    return True

def dfs(x):
    global res

    if x == n:
        res += 1
    else:
        for i in range(n):
            if visit[i]:
                continue
            row[x] = i
            if not_adj(x):
                visit[i] = 1
                dfs(x+1)
                visit[i] = 0

n = int(input())
row = [0]*n
visit = [0]*n
res = 0
dfs(0)
print(res)


"""
Method 1

시간 초과
"""

import sys
input = sys.stdin.readline

def not_adj(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x-i:
            return False
    return True

def dfs(x):
    global res

    if x == n:
        res += 1
    else:
        for i in range(n):
            row[x] = i
            if not_adj(x):
                dfs(x+1)

n = int(input())
row = [0]*n
res = 0
dfs(0)
print(res)



