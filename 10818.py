idx, v = 0, 0
for i in range(9):
    n = int(input())
    if v < n:
        idx = i+1
        v = n
print(v)
print(idx)
