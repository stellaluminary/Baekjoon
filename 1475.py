"""
Method 3

"""

r = [0 for i in range(9)]
for i in list(input()):
    if i in ['6', '9']:
        r[6] += 1
    else:
        r[int(i)] += 1
if r[6] % 2 == 0:
    r[6] //= 2
else:
    r[6] = r[6] // 2 + 1

print(max(r))


"""
Method 2

"""
import math

r = [0 for i in range(10)]
for i in list(map(int, input())):
    r[i] += 1
r[6] = math.ceil((r[6]+r[9])/2)
print(max(r[:9]))

"""
Method 1

"""
import math
n = list(input())
d = {}
for i in range(10):
    d[str(i)] = 0
for i in n:
    d[i] += 1

maxi = 0
s_n = 0

for j in d:
    if j == '6' or j == '9':
        s_n += d[j]
        continue
    maxi = max(maxi, d[j])

print(max(maxi, math.ceil(s_n/2)))



#66 929 66 66 66 66 6\
#66929666666666