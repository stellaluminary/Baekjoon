"""
Method 4

"""


n = input()
res = 0
for i in range(1, len(n)):
    res += 9 * 10**(i-1) * i
res += (int(n)-10**(len(n)-1)+1)*len(n)
print(res)

"""
Method 3

"""

n = input()
length = len(n)
res = length * (int(n) - 10**(length - 1) + 1)
length -= 1
while length:
    res += length * (10**length - 10**(length - 1))
    length -= 1
print(res)




"""
Method 2

시간 초과
"""

st = ''
for i in range(1, int(input())+1):
    st += str(i)
print(len(st))

"""
Method 1

메모리 초과
"""

st = ''.join([str(i) for i in range(1, int(input())+1)])
print(len(st))