"""
Method 2

"""
from itertools import permutations
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in permutations(a):
    t = 0
    for j in range(1, n):
        t += abs(i[j - 1] - i[j])
    if t > ans:
        ans = t
print(ans)


"""
Method 1

62 [8, 20, 1, 15, 4, 10]

"""
import copy
n = int(input())
a = list(map(int, input().split()))

visit = [0] * n
max_v = 0
def dfs(depth, arr):
    global n, max_v
    if depth == n:
        tmp_m = 0
        for i in range(1, n):
            tmp_m += abs(arr[i-1] - arr[i])
        if tmp_m > max_v:
            max_v = tmp_m
        return

    for i in range(n):
        if not visit[i]:
            visit[i] = 1
            tmp = copy.deepcopy(arr)
            tmp.append(a[i])
            dfs(depth + 1, tmp)
            visit[i] = 0

dfs(0, [])
print(max_v)

"""
Method 1 다른 버전

"""

n = int(input())
a = list(map(int, input().split()))
t = []
visit = [0] * n
ans = 0
def dfs(depth):
    global n, ans
    if depth == n:
        total = 0
        for i in range(1, n):
            total += abs(t[i-1] - t[i])
        ans = max(ans, total)
        return

    for i in range(n):
        if not visit[i]:
            visit[i] = 1
            t.append(a[i])
            dfs(depth + 1)
            visit[i] = 0
            t.pop()
dfs(0)
print(ans)

