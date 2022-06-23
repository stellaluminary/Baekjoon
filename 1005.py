"""
Method 1

"""
from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    indegree = [0]*(n+1)
    time = [0] + list(map(int, input().split()))
    dp = [0 for _ in range(n+1)]

    for i in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i]

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[now]+time[i], dp[i])
            if indegree[i] == 0:
                q.append(i)

    idx = int(input())
    print(dp[idx])






"""
Method 2

"""






"""
Method 3

"""