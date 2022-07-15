"""
Method 3

"""

"""
Method 2

"""
n, l = map(int, input().split())
loc, time = 0, 0

for _ in range(n):
    c, r, g = map(int, input().split())
    time += c - loc
    loc = c
    if time % (r+g) < r:
        time += (r - time % (r+g))
time += l-loc
print(time)

"""
Method 1

"""

n, l = map(int, input().split())
tl = []

for _ in range(n):
    loc, r, g = map(int, input().split())
    tl.append([loc, r, g])

tl.append([l,0,0])
time = tl[0][0]

for i in range(n):
    interval = time % (tl[i][1] + tl[i][2])
    if interval < tl[i][1]:
        time += tl[i][1] - interval
    time += tl[i+1][0] - tl[i][0]

print(time)




