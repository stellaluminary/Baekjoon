"""
Method 2

"""
n,start,end=map(int, input().split())
cnt=0
while start!=end:
  start -= start//2
  end -= end//2
  cnt+=1
print(cnt)

"""
Method 1

"""

n, j, h = map(int, input().split())
round = 1
while 1:
    if abs(j-h) == 1 and j//2 != h//2:
        print(round)
        break

    if j % 2 == 1:
        j = (j+1)//2
    else:
        j //= 2

    if h % 2 == 1:
        h = (h + 1) // 2
    else:
        h //= 2

    round += 1












