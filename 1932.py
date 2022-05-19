# n=5
# l=[
#     [7],
#     [3,8],
#     [8,1,0],
#     [2,7,4,4],
#     [4,5,2,6,5]
# ]

n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

t = [[0]*i for i in range(1,n+1)]
t[0][0] = l[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            t[i][j] += l[i][j] + t[i-1][0]
        elif j == i:
            t[i][j] += l[i][j] + t[i-1][j-1]
        else:
            t[i][j] += l[i][j] + max(t[i-1][j-1], t[i-1][j])

print(max(t[-1]))



