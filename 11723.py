"""
Method 3

"""
import sys
s = set()

for i in range(int(input())):
    a = sys.stdin.readline().rstrip().split()
    if len(a) == 1:
        if a[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()
        continue

    func, v = a[0], int(a[1])

    if func == 'add':
        s.add(v)
    elif func == 'remove':
        s.discard(v)
    elif func == 'check':
        print(1 if v in s else 0)
    elif func == 'toggle':
        if v in s:
            s.discard(v)
        else:
            s.add(v)


"""
Method 2
시간 초과
"""
import sys
s = set()

for i in range(int(input())):
    a = sys.stdin.readline().rstrip().split()
    if len(a) == 1:
        if a[0] == 'all':
            s = set([str(i) for i in range(1, 21)])
        else:
            s = set()
        continue

    if a[0] == 'add':
        s.add(a[1])
    elif a[0] == 'remove':
        s.discard(a[1])
    elif a[0] == 'check':
        print(1 if a[1] in s else 0)
    elif a[0] == 'toggle':
        if a[1] in s:
            s.discard(a[1])
        else:
            s.add(a[1])

"""
Method 1
시간 초과
"""

s = []
for i in range(int(input())):
    a = list(input().split())
    if a[0] == 'add':
        if a[1] not in s:
            s.append(a[1])
    elif a[0] == 'remove':
        if a[1] in s:
            del s[s.index(a[1])]
    elif a[0] == 'check':
        if a[1] in s:
            print(1)
        else:
            print(0)
    elif a[0] == 'toggle':
        if a[1] in s:
            del s[s.index(a[1])]
        else:
            s.append(a[1])
    elif a[0] == 'all':
        s = [str(i) for i in range(1, 21)]
    elif a[0] == 'empty':
        s = []


