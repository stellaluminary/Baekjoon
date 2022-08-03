"""
Method 3

"""

n = int(input())
f = int(input())
n -= n%100
res = f - n%f
if res == f:
    res = 0
print('%02d' %res)

"""
Method 2

"""
n = input()
f = int(input())
nw = int(n[:-2]+'00')
while 1:
    if nw % f == 0:
        break
    nw += 1
print(str(nw)[-2:])

"""
Method 1

"""

n = int(input())
f = int(input())
for i in range(n//100*100, (n//100+1)*100):
    if i % f == 0:
        print((str(i%100)).zfill(2))
        break


