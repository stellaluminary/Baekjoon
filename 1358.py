w,h,x,y,p = map(int, input().split())
cnt = 0
r = h//2
for i in range(p):
    px, py = map(int, input().split())

    if (px-x)**2 + (py - (y+r))**2 <= r**2:
        cnt += 1
    elif x <= px <= x+w and y <= py <= y+h:
        cnt += 1
    elif (px-(x+w))**2 + (py - (y+r))**2 <= r**2:
        cnt += 1
print(cnt)
