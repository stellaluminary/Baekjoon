import sys
input = sys.stdin.readline

l = []
for i in range(int(input())):
    l.append(list(map(int, input().split())))
l.sort()
for i in range(len(l)):
    print(*l[i])