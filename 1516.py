"""
Method 1

"""
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
time = [0]

for i in range(1, n+1):
    t = list(map(int, input().split()))
    time.append(t[0])
    for j in t[1:-1]:
        graph[j].append(i)
        indegree[i] += 1


res = [0] * (n + 1)
q = deque()

for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)
        res[i] = time[i]

while q:
    now = q.popleft()
    for k in graph[now]:
        indegree[k] -= 1
        res[k] = max(res[now]+time[k], res[k])
        if indegree[k] == 0:
            q.append(k)

for i in res[1:]:
    print(i)

