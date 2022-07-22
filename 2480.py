"""
Method 3

"""
a, b, c = map(int, input().split())

if a == b == c :
  print(10000 + a * 1000)
elif a == b :
  print(1000 + a * 100)
elif a == c :
  print(1000 + a * 100)
elif b == c :
  print(1000 + b * 100)
else :
  print(max(a, b, c) * 100)

"""
Method 2

"""
arr = list(map(int, input().split()))

s = set(arr)
if len(s) == 1:
    print(10000+arr[0]*1000)
elif len(s) == 3:
    print(max(arr) * 100)
else:
    for i in range(3):
        if arr.count(arr[i]) == 2:
            val = arr[i]
            break
    print(1000 + val*100)

"""
Method 1

"""
a,b,c = map(int, input().split())

s = set([a, b, c])
if len(s) == 1:
    print(10000+a*1000)
elif len(s) == 3:
    print(max(a, b, c) * 100)
elif len(s) == 2:
    d = {i:0 for i in s}
    for i in [a, b, c]:
        d[i] += 1
    for i in [a, b, c]:
        if d[i] == 2:
            val = i
            break
    print(1000 + val*100)


