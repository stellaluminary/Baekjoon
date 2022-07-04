"""
Method 3

"""

import sys
input = sys.stdin.readline

for i in range(int(input())):
    p = input().rstrip()
    n = int(input())
    l = input().rstrip()[1:-1].split(',')
    p = p.replace('RR','')

    if n == 0:
        l = []

    rev, f, b = 0, 0, 0
    flag = False

    for j in p:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if rev % 2 == 0:
                f += 1
            else:
                b += 1

    l = l[f:n-b]

    if f + b > n:
        print('error')
    else:
        if rev % 2 == 0:
            print('[' + ','.join(l) + ']')
        else:
            l.reverse()
            print('[' + ','.join(l) + ']')

"""
Method 2

"""

import sys
input = sys.stdin.readline

for i in range(int(input())):
    p = input().rstrip()
    n = int(input())
    l = input().rstrip()[1:-1].split(',')

    if n == 0:
        l = []

    rev = 0
    flag = False

    for j in p:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(l) == 0:
                flag = True
                print('error')
                break
            else:
                if rev % 2 == 0:
                    l.pop(0)
                else:
                    l.pop()

    if not flag:
        if rev % 2 == 0:
            print('[' + ','.join(l) + ']')
        else:
            l.reverse()
            print('[' + ','.join(l) + ']')


"""
Method 1

"""

import sys
input = sys.stdin.readline

for i in range(int(input())):
    p = list(input())
    n = int(input())
    l = input()
    if n == 0:
        l = []
    else:
        l = l[1:-2].split(',')

    flag = False
    for j in p:
        if j == 'R':
            l = [l[i] for i in range(len(l)-1, -1, -1)]
        elif j == 'D':
            if len(l) == 0:
                flag = True
                break
            else:
                l.pop(0)

    if flag:
        print('error')
    else:
        print('[' + ','.join(l) + ']')
