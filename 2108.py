"""
Method 1

"""
from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
l.sort()

print(round(sum(l)/n))
print(l[n//2])

cnt = Counter(l).most_common(2)
if len(cnt) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(l[-1]-l[0])


"""
Method 2

"""

from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
l.sort()

print(round(sum(l)/n))
print(l[n//2])

cnt = Counter(l)
t = []
res = 0
for i in cnt:
    if res < cnt[i]:
        res = cnt[i]
        t = [i]
    elif res == cnt[i]:
        t.append(i)
if len(t) == 1:
    print(t[0])
else:
    print(t[1])

print(l[-1]-l[0])



