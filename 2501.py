"""
Method 3

"""

"""
Method 2

"""
n,k = map(int, input().split())
t = [i for i in range(1, n+1) if n%i == 0]
print(0 if len(t)<k else t[k-1])

"""
Method 1

"""
n,k = map(int, input().split())
t = []
for i in range(1, n//2+1):
    if n % i == 0:
        t.append(i)
t.append(n)
if len(t) >= k:
    print(t[k-1])
else:
    print(0)






