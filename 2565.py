"""
Method 1
"""
import sys
input = sys.stdin.readline
n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
l.sort()
d=[1]*n
for i in range(n):
    for j in range(i):
        if l[i][1] > l[j][1]:
            d[i] = max(d[i], d[j]+1)
print(n-max(d))

"""
Wrong
"""
import sys
input = sys.stdin.readline
# n = int(input())
# l = [list(map(int, input().split())) for _ in range(n)]

n=8
l=[[1,8], [3,9],[2,2],[4,1],[6,4],[10,10],[9,7],[7,6]]

# def ck(x, y):
#     if x[0] > y[0] and x[1] < y[1]:
#         return True
#     elif x[0] < y[0] and x[1] > y[1]:
#         return True
#     else:
#         return False
#
# def intsec(d, l):
#     for i in range(len(l)):
#         for j in range(len(l)):
#             if i != j:
#                 d[i] += ck(l[i], l[j])
#     return d,l
#
# for i in range(n):
#     d = [0] * len(l)
#     d, l = intsec(d, l)
#     if d == [0] * len(l):
#         break
#     maxidx = d.index(max(d))
#     l.pop(maxidx)

#print(i)








