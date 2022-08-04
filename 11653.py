"""
Method 2

"""
n = int(input())
k = 2
while n != 1:
    if n % k == 0:
        print(k)
        n /= k
    else:
        k += 1

"""
Method 1
시간 초과
"""

n = int(input())
p = []
for i in range(2,n+1):
    flag = False
    for j in range(2, i):
        if i % j == 0:
            flag = True
            break
    if not flag and n % i == 0:
        p.append(i)
k = 0
while 1:
    if n == 1:
        break

    if n % p[k] == 0:
        print(p[k])
        n /= p[k]
    else:
        k += 1

