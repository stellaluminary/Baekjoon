"""
Method 2

"""
e,s,m = map(int, input().split())
y = 1
while 1:
    if (y-e) % 15 == 0 and (y-s) % 28 == 0 and (y-m) % 19 == 0:
        break
    y += 1
print(y)


"""
Method 1

"""

ans = list(map(int, input().split()))
o = [1,1,1]
cnt = 1
while o != ans:
    cnt += 1
    for i in range(3):
        o[i] += 1
        if o[0] == 16:
            o[0] = 1
        if o[1] == 29:
            o[1] = 1
        if o[2] == 20:
            o[2] = 1
print(cnt)