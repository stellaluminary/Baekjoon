"""
Method 3

"""

"""
Method 2

"""
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    l = [input().rstrip() for _ in range(n)]
    l.sort()
    flag = False
    for i in range(n-1):
        if l[i] == l[i+1][:len(l[i])]:
            flag = True
            break

    if flag:
        print('NO')
    else:
        print('YES')


"""
Method 1

"""

import sys
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    l = [input().rstrip() for _ in range(n)]
    l.sort(key=len)

    flag = False
    for p in range(n-1):
        for q in range(p+1, n):
            if l[p] in l[q]:
                flag = True
                break
        if flag:
            break

    if flag:
        print('NO')
    else:
        print('YES')