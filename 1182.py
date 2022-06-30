def visual(l):
    for i in l:
        print(i)

"""
Method 3

"""

"""
Method 2

"""
def dfs(idx, total):
    global cnt

    if idx >= n:
        return
    total += l[idx]
    if total == s:
        cnt += 1

    dfs(idx+1, total)
    dfs(idx+1, total - l[idx])


import sys
input = sys.stdin.readline

n,s = map(int, input().split())
l = list(map(int, input().split()))
cnt = 0
dfs(0, 0)
print(cnt)

"""
Method 1

"""

def dfs(idx, total):
    global s
    if idx >= 1 and total == s:
        tmp = ' '.join(map(str, visit))
        if tmp not in o:
            o.append(tmp)
        return

    for i in range(idx, n):
        if not visit[i]:
            visit[i] = 1
            dfs(idx+1, total + l[i])
            visit[i] = 0


import sys
input = sys.stdin.readline

n,s = map(int, input().split())
l = list(map(int, input().split()))
visit = [0]*n
o = []
dfs(0, 0)
print(len(o))


