import sys
input = sys.stdin.readline

l = []
for i in range(int(input())):
    a, n = input().split()
    l.append([int(a), n])
l.sort(key=lambda x: x[0])
for i in l:
    print(*i)