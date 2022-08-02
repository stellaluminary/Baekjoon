"""
Method 1

"""

n = int(input())
graph = [[0] * 101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in range(n) :
    y, x, d, g = map(int, input().split())
    graph[x][y] = 1

    curve = [d]
    for j in range(g):
        for k in range(len(curve) - 1, -1, -1):
            curve.append((curve[k] + 1) % 4)
    print(curve)

    for j in range(len(curve)):
        x += dx[curve[j]]
        y += dy[curve[j]]
        if not 0 <= x < 101 or not 0 <= y < 101:
            continue
        graph[x][y] = 1

    for i in range(10):
        print(*graph[i][:10])


result = 0
for i in range(100):
    for j in range(100):
        if [graph[i][j],graph[i+1][j], graph[i][j+1], graph[i+1][j+1]] == [1,1,1,1]:
            result += 1
print(result)