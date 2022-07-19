"""
Method 1

다익스트라
"""

import heapq
import sys
input = sys.stdin.readline
INF = 1e9

v,e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distance = [INF]*(v+1)

for i in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijstra(start)

for i in range(1, v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])



