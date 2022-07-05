"""
Method 2

"""
import sys
input = sys.stdin.readline

s = input().rstrip()
o = input().rstrip()
dp = [[0]*(len(s)+1) for _ in range(len(o)+1)]
ans = 0

for i in range(1, len(o)+1):
    for j in range(1, len(s)+1):
        if o[i-1] == s[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            ans = max(ans, dp[i][j])

print(ans)


"""
Method 1

"""

import sys
input = sys.stdin.readline

s = list(input().rstrip())
o = list(input().rstrip())
ans = 0
for i in range(len(s)):
    for j in range(len(o)):
        k = 1
        while 1:
            if s[i:i+k] == o[j:j+k] and i+k <= len(s) and j+k <= len(o):
                k += 1
            else:
                break
        ans = max(ans, k-1)
print(ans)