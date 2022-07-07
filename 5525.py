"""
Method 3

"""

"""
Method 2

"""
n = int(input())
m = int(input())
s = input()
ans, i, cnt = 0, 0, 0

while i <= (m-2):
    if s[i:i+3] == 'IOI':
        i += 2
        cnt += 1
        if cnt == n:
            ans += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0

print(ans)

"""
Method 1

시간 초과
"""

n = int(input())
m = int(input())
s = input()
p = 'IO'*n + 'I'
cnt = 0

for i in range(m-len(p)):
    if s[i:i+len(p)] == p:
        cnt += 1
print(cnt)