"""
Method 2

"""
def prime(k):
    if k == 1:
        return 0

    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return 0
    return 1

prime_list = []

for i in range(2,123456*2+1):
    if prime(i):
        prime_list.append(i)

while 1:
    n = int(input())

    if n == 0:
        break
    cnt = 0
    for i in prime_list:
        if i > 2*n:
            break
        elif n < i <= 2*n:
            cnt += 1
    print(cnt)




"""
Method 1
시간 초과
"""

def prime(k):
    if k == 1:
        return 0

    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return 0
    return 1

while 1:
    n = int(input())

    if n == 0:
        break
    cnt = 0
    for i in range(n+1, 2*n+1):
        if prime(i):
            cnt += 1
    print(cnt)