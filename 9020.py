"""
Method 3

"""

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

for i in range(int(input())):
    ans = []
    n = int(input())

    for j in range(n//2, 0, -1):
        if prime(j) and prime(n-j):
            print(j, n-j)
            break

"""
Method 1

"""
def prime(k):
    if k == 1:
        return 0

    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return 0
    return 1

prime_list = []

for i in range(2, 10000+1):
    if prime(i):
        prime_list.append(i)

for i in range(int(input())):
    ans = []
    n = int(input())

    for j in prime_list:
        if n - j in prime_list:
            ans.append((abs(j-(n-j)), j, n-j))
    ans.sort()
    print(ans[0][1], ans[0][2])