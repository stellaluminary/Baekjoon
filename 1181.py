"""
Method 3

"""
import sys
input = sys.stdin.readline

n = int(input())
l = [input().rstrip() for i in range(n)]
l = list(set(l))
t = []
for i in l:
    t.append((len(i), i))

t.sort()

for length, word in t:
    print(word)

"""
Method 2

"""
import sys
input = sys.stdin.readline

n = int(input())
l = [input().rstrip() for i in range(n)]
l = list(set(l))
l.sort()
l.sort(key=len)

for i in l:
    print(i)

"""
Method 1

"""

import sys
input = sys.stdin.readline

n = int(input())
l = [input().rstrip() for i in range(n)]

t = [[] for _ in range(51)]

for i in range(len(l)):
    t[len(l[i])].append(l[i])

for i in range(len(t)):
    if len(t[i]) == 0:
        continue
    elif len(t[i]) == 1:
        print(t[i][0])
    else:
        t[i] = list(set(t[i]))
        t[i].sort()
        for j in range(len(t[i])):
            print(t[i][j])

