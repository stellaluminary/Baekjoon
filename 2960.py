"""
Method 2

"""

n,k = map(int, input().split())
s = [1]*(n+1)
cnt = 0
flag = False
for i in range(2, n+1):
    for j in range(i, n+1, i):
        if s[j]:
            s[j] = 0
            cnt += 1
            if cnt == k:
                print(j)
                flag = True
                break
    if flag:
        break


"""
Method 1

"""

n,k = map(int, input().split())
s = [i for i in range(2, n+1)]
cnt = 0
flag = False
while len(s) != 0:
    p = s[0]
    for i in range(len(s)):
        if s[i] % p == 0:
            cnt += 1
            tmp = s[i]
        if cnt == k:
            flag = True
            break
    if flag:
        break
    s = [i for i in s if i % p != 0]
print(tmp)

