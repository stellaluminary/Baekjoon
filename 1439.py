"""
Method 2

"""

n = input()
cnt = 0
for i in range(len(n)-1):
    if n[i] != n[i+1]:
        cnt += 1

print((cnt+1)//2)


"""
Method 1

"""

n = list(input())
s = n[0]
for i in range(1, len(n)):
    if s[-1] != n[i]:
        s += n[i]
t = list(s)
print(min(t.count('1'), t.count('0')))