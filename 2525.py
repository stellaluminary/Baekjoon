h, m = map(int, input().split())
c = int(input())

h = (h + (c + m) // 60) % 24
m = (c + m) % 60
print(h, m)