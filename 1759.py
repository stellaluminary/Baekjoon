"""
Method 4

"""

import sys
from itertools import combinations

input = sys.stdin.readline
l, n = map(int, input().split())
c = sorted(list(input().split()))

for s in combinations(c, l):
    m = 0
    for i in range(l):
        if s[i] in 'aeiou':
            m += 1
    if m >= 1 and l-m >= 2:
        print(''.join(s))

"""
Method 3

"""

def dfs(step, total):
    if len(total) == l:
        aeiou = 0
        for i in total:
            if i in 'aeiou':
                aeiou += 1
        if aeiou >= 1 and len(total) - aeiou >=2:
            print(total)
        return
    if step == n:
        return

    dfs(step + 1, total+c[step])
    dfs(step + 1, total)

import sys
input = sys.stdin.readline

l, n = map(int, input().split())
c = sorted(list(input().split()))
dfs(0, '')

"""
Method 2

"""

def dfs(step, idx):
    global res
    if step == l:
        aeiou = 0
        for i in res:
            if i in 'aeiou':
                aeiou += 1
        if aeiou >= 1 and len(res) - aeiou >=2:
            print(res)
        return

    for i in range(idx, n):
        if not visit[i]:
            visit[i] = 1
            res += c[i]
            dfs(step+1, i+1) # idx = i+1이 되는 것이 key
            visit[i] = 0
            res = res[:-1]

import sys
input = sys.stdin.readline

l, n = map(int, input().split())
c = sorted(list(input().split()))
visit = [0] * n
res = ''
dfs(0, 0)

"""
Method 1

"""

def dfs(step):
    global res
    if step == l:
        mo_cnt = 0
        ja_cnt = 0
        for i in res:
            if i in mo:
                mo_cnt += 1
            else:
                ja_cnt += 1

        if mo_cnt >= 1 and ja_cnt >=2:
            print(res)
        return

    for i in range(step, n):
        if not visit[i] and (len(res) == 0 or ord(res[-1]) < ord(c[i])):
            visit[i] = 1
            res += c[i]
            dfs(step+1)
            visit[i] = 0
            res = res[:-1]



import sys
input = sys.stdin.readline

l, n = map(int, input().split())
c = sorted(list(input().split()))
visit = [0] * n
res = ''
mo = ['a', 'e', 'i', 'o', 'u']
dfs(0)
