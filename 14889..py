"""
Method 2

"""

def dfs(depth, idx):
    global n, res
    if depth == n//2:
        p1, p2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]:
                    p1 += s[i][j]
                elif not visit[i] and not visit[j]:
                    p2 += s[i][j]
        res = min(res, abs(p1-p2))
        return

    for i in range(idx, n):
        if not visit[i]:
            visit[i] = 1
            dfs(depth+1, i+1)
            visit[i] = 0

import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
visit = [0] * n
res = 1e3
dfs(0, 0)
print(res)


"""
Method 1

"""
from itertools import combinations

def ability(ck_l):
    q = 0
    for k in combinations(ck_l, 2):
        q += s[k[0]][k[1]] + s[k[1]][k[0]]
    return q

def dfs(num):
    global n, res
    if num == n//2:
        o1 = []
        o2 = []
        for j in range(n):
            if ck[j]:
                o1.append(j)
            else:
                o2.append(j)

        print(ability(o1), ability(o2), abs(ability(o1) - ability(o2)))
        res = min(res, abs(ability(o1) - ability(o2)))
        return

    for i in range(n):
        for j in range(i+1, n):
            if (i, j) not in visit:
                visit.append((i, j))
                ck[i], ck[j] = 1, 1
                print('before dfs i,j', i, j, visit, ck)
                dfs(sum(ck))
                print('after dfs i,j', i, j, visit, ck)
                visit.pop()
                ck[i], ck[j] = 0, 0

import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
visit = []
ck = [0] * n
res = 1e3
dfs(0)
print(res)
