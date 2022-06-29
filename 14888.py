"""
Method 3

"""

"""
Method 2

"""
import sys
input = sys.stdin.readline

def dfs(idx):
    global ans, maxR, minR
    if idx == n:
        maxR = max(maxR, ans)
        minR = min(minR, ans)
        return

    for i in range(4):
        tmp = ans
        if o[i] == 0:
            continue

        if i == 0:
            ans += a[idx]
        elif i == 1:
            ans -= a[idx]
        elif i == 2:
            ans *= a[idx]
        elif i == 3:
            if ans < 0:
                ans = -(abs(ans) // a[idx])
            else:
                ans //= a[idx]
        o[i] -= 1
        dfs(idx+1)
        ans = tmp
        o[i] += 1

n = int(input())
a = list(map(int, input().split()))
o = list(map(int, input().split()))

ans = a[0]
maxR = -(1e9)
minR = 1e9
dfs(1)
print(maxR)
print(minR)


"""
Method 1

"""

import sys
input = sys.stdin.readline

def dfs(idx):
    if sum(o) == 0:
        sv.append(t[-1])
        return

    for j in range(4):
        if o[j] == 0:
            continue

        if j == 0:
            t.append(t[-1] + a[idx])
        elif j == 1:
            t.append(t[-1] - a[idx])
        elif j == 2:
            t.append(t[-1] * a[idx])
        elif j == 3:
            if t[-1] < 0:
                tmp = -(abs(t[-1]) // a[idx])
            else:
                tmp = t[-1] // a[idx]
            t.append(tmp)
        o[j] -= 1
        dfs(idx+1)
        t.pop()
        o[j] += 1

n = int(input())
a = list(map(int, input().split()))
o = list(map(int, input().split()))

t = [a[0]]

sv = []
dfs(1)

sv.sort()
print(sv[-1])
print(sv[0])



