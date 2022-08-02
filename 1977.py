"""
Method 2

"""

n = int(input())
m = int(input())
t = [i**2 for i in range(101) if n <= i**2 <= m]
print(f'{sum(t)}\n{t[0]}'if t else -1)

"""
Method 1

"""
n = int(input())
m = int(input())
t = [i**2 for i in range(1,101)]
s = []
for i in t:
    if n <= i <= m:
        s.append(i)
if len(s):
    print(sum(s))
    print(min(s))
else:
    print(-1)