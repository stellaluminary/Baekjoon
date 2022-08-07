x = int(input())
n = int(input())
for i in range(n):
    p, a = map(int, input().split())
    x -= p*a
print('Yes' if x == 0 else 'No')