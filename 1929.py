"""
Method 2

"""

n, m = map(int, input().split())

def prime(k):
    if k == 1:
        return 0

    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return 0
    return 1

for i in range(n, m+1):
    if prime(i):
        print(i)

"""
Method 1
시간 초과
"""

n, m = map(int, input().split())

for i in range(n,m+1):
    flag = False
    for j in range(2, i):
        if i % j == 0:
            flag = True
            break
    if not flag:
        print(i)