"""
Method 1

"""
n = list(map(int, input()))
n.sort(reverse=True)
if n[-1] == 0 and sum(n) % 3 == 0:
    print(''.join(map(str, n)))
else:
    print(-1)

