"""
Method 2

"""

from itertools import combinations
d = [int(input()) for _ in range(9)]
for i in combinations(d, 7):
    if sum(i) == 100:
        n = i
        break
print('\n'.join(map(str,i)))

"""
Method 1

"""

l = [int(input()) for _ in range(9)]

for i in range(8):
    for j in range(i+1, 9):
        if sum(l) - (l[i]+l[j]) == 100:
            m = [l[i], l[j]]
            break

l.remove(m[0])
l.remove(m[1])
print('\n'.join(map(str, l)))






