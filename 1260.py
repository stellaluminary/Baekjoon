"""
Method 1
"""

# n,m,v = 4,5,1
# l=[[],[2,3,4],[1,4],[1,4],[1,2,3]]
#
# n,m,v = 5,5,3
# l=[[],[2,3],[1,5],[1,4],[3,5],[2,4]]

# n,m,v = map(int, input().split())
# l= [[] for _ in range(n+1)]
#
# for i in range(m):
#     a, b = map(int, input().split())
#     l[a].append(b)
#     l[b].append(a)
#
# for i in range(n+1):
#     l[i].sort()
#
# from collections import deque
#
# visited = [False]*(n+1)
# visited2 = [False]*(n+1)
#
# # dfs
# def dfs(graph, idx, visited):
#     print(idx, end=' ')
#     for i in graph[idx]:
#         if not visited[i]:
#             dfs(graph, i, visited)
#
# # bfs
# def bfs(graph, start, visited2):
#     queue = deque([start])
#     visited2[start] = True
#     while queue:
#         v = queue.popleft()
#         print(v, end=' ')
#
#         for i in graph[v]:
#             if not visited2[i]:
#                 queue.append(i)
#                 visited2[i] = True
#
# dfs(l, v, visited)
# print()
# bfs(l, v, visited2)


"""
Method 2
"""

n,m,v = map(int, input().split())
l= [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    l[a][b] = l[b][a] = 1

visit = [False]*(n+1)

# dfs
def dfs(v):
    visit[v] = True
    print(v, end=' ')
    for i in range(1, n+1):
        if visit[i] == 0 and l[v][i] == 1:
            dfs(i)

# bfs
def bfs(v):
    queue = [v]
    visit[v] = False
    while queue:
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, n+1):
            if visit[i] == 1 and l[v][i] == 1:
                queue.append(i)
                visit[i] = False

dfs(v)
print()
bfs(v)





