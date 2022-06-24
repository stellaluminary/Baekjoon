"""
Method 1

"""


import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):

    n, m = map(int, input().split())
    l = list(map(int, input().split()))

    o = [[l[i], i] for i in range(n)]

    cnt = 0
    while o:
        now = o.pop(0)
        ck_F = False
        for i in o:
            if now[0] < i[0]:
                o.append(now)
                ck_F = True
                break

        if ck_F == True:
            continue
        elif ck_F == False:
            cnt += 1

        if m == now[1]:
            print(cnt)
            break


"""
Method 2

"""
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    idx = [i for i in range(n)]
    cnt = 0

    while l:
        if l[0] == max(l):
            cnt += 1
            if idx[0] == m:
                print(cnt)
                break
            l.pop(0)
            idx.pop(0)
        else:
            l.append(l.pop(0))
            idx.append(idx.pop(0))












