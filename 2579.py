# n=6
# l=[0,10,20,15,25,10,20]

"""
# Method 1
n = int(input())
a = [int(input()) for i in range(n)]

t = []
t.append(a[0])
if n>1:
    t.append(a[0] + a[1])
if n>2:
    t.append(max(t[0] + a[2], a[1] + a[2]))

for i in range(3, n):
    t.append(max(t[i - 3] + a[i] + a[i - 1], t[i - 2] + a[i]))

print(t[-1])
"""

# Method 2
def s(n, a, dp):
  if n == 1:
    dp[1]=a[1]
    return dp[1]
  elif n == 2:
    dp[2]=a[1]+a[2]
    return dp[2]
  elif n==3:
    dp[3] = max(a[1]+a[3], a[2]+a[3])
    return dp[3]

  if dp[n]:
    pass
  else:
    dp[n]=max(s(n-3,a,dp)+a[n]+a[n-1],s(n-2,a,dp)+a[n])
  return dp[n]

n = int(input())
a = [0]
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
  a.append(int(input()))

print(s(n, a, dp))