"""
Method 2

"""

s = input()
t = input()
res = 0
flag = False

while len(t) > len(s):
    if t[-1] == 'A':
        t = t[:-1]
    elif t[-1] == 'B':
        t = t[:-1]
        t = t[::-1]
    if s == t:
        flag = True
        break

if flag:
    print(1)
else:
    print(0)


"""
Method 1

"""

s = input()
t = input()

res = [s]
for i in range(len(t) - len(s)):
    tmp = []
    for j in range(len(res)):
        a = res[j] + 'A'
        b = res[j][::-1] + 'B'

        if len(a) == len(t):
            if a == t:
                tmp.append(a)
            if b == t:
                tmp.append(b)
            break

        if a in t or a[::-1] in t:
            tmp.append(a)
        if b in t or b[::-1] in t:
            tmp.append(b)
    res = tmp[:]

if len(res):
    print(1)
else:
    print(0)



