"""
Method 1

"""
import sys
input = sys.stdin.readline

n = int(input())
l = [0]*10001

for i in range(n):
    n = int(input())
    l[n] += 1

for i in range(len(l)):
    for j in range(l[i]):
        print(i)


"""
메모리 초과 - Method 2

"""

n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

l.sort()
for i in range(n):
    print(l[i])
