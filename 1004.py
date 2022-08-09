import sys
input = sys.stdin.readline

def circle(x,y,x1,y1, r):
    if (x-x1)**2 + (y-y1)**2 <= r**2:
        return 1
    else:
        return 0

for _ in range(int(input())):
    x1,y1,x2,y2 = map(int, input().split())
    planet = [list(map(int, input().split())) for _ in range(int(input()))]
    cnt = 0
    for x,y,r in planet:
        if circle(x,y,x1,y1,r) + circle(x,y,x2,y2,r) == 1:
            cnt += 1
    print(cnt)