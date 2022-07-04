"""
Method 1

"""

a,b = input().split()
res = 51
for i in range(len(b)-len(a)+1):
    cnt = 0
    tb = b[i:i+len(a)]
    for j in range(len(a)):
        if a[j] != tb[j]:
            cnt += 1
    res = min(res, cnt)
print(res)

