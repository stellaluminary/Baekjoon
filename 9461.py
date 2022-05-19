import sys
input = sys.stdin.readline

l = [0,1,1,1,2,2] + [0]*96
for i in range(6,101):
    l[i] = l[i-1] + l[i-5]

for i in range(int(input())):
    t = int(input())
    print(l[t])

