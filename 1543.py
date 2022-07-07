"""
Method 3

"""

print(input().count(input()))

"""
Method 2

"""
s = input()
t = input()
cnt = 0
n = 0
while n <= len(s) - len(t):
    if s[n:n+len(t)] == t:
        cnt += 1
        n += len(t)
    else:
        n += 1
print(cnt)



"""
Method 1

"""

s = input()
t = input()
cnt = 0

while t in s:
    for i in range(len(s)):
        if s[i:i+len(t)] == t:
            s = s[i+len(t):]
            break
    cnt += 1

print(cnt)