#n=3
#l = [[26,40,83],[49,60,57],[13,89,99]]

#n=8
#l = [[71, 39, 44],[32, 83, 55],[51, 37, 63],[89, 29, 100],[83, 58, 11],[65, 13, 15],[47, 25, 29],[60, 66, 19]]

""""
n = int(input())
l = [[0]*3 for _ in range(n)]
t = [[0]*3 for _ in range(n)]

for i in range(n):
    l[i][0], l[i][1], l[i][2] = map(int, input().split())

for i in range(n):
    if i == 0:
        t[i][0] = l[i][0]
        t[i][1] = l[i][1]
        t[i][2] = l[i][2]
        continue
    t[i][0] = l[i][0] + min(t[i-1][1], t[i-1][2])
    t[i][1] = l[i][1] + min(t[i-1][0], t[i-1][2])
    t[i][2] = l[i][2] + min(t[i-1][0], t[i-1][1])

print(min(min(t[n-1][0], t[n-1][1]), t[n-1][2]))
"""
import sys

n = int(input())
l = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
    l[i][0] += min(l[i-1][1], l[i-1][2])
    l[i][1] += min(l[i-1][0], l[i-1][2])
    l[i][2] += min(l[i-1][0], l[i-1][1])

print(min(l[n-1]))
