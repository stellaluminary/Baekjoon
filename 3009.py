"""
Method 2

"""
x = []
y = []

for i in range(3):
    a,b = map(int,input().split())

    if a in x : x.remove(a)
    else : x.append(a)
    if b in y : y.remove(b)
    else : y.append(b)

print(*x,*y)

"""
Method 1

"""


h,v = {},{}
for i in range(3):
    a,b = map(int, input().split())
    if a not in h:
        h[a] = 1
    else:
        del h[a]

    if b not in v:
        v[b] = 1
    else:
        del v[b]

for i,j in zip(h.keys(), v.keys()):
    print(i,j)