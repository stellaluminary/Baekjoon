"""
Method 2

"""

n = int(input())
mw, mh = 0, 0
mw_idx, mh_idx = 0, 0
l=[]
for i in range(6):
    tmp = list(map(int, input().split()))
    l.append(tmp)
    if tmp[0] == 1 or tmp[0] == 2:
        if mw < tmp[1]:
            mw = tmp[1]
            mw_idx = i
    elif tmp[0] == 3 or tmp[0] == 4:
        if mh < tmp[1]:
            mh = tmp[1]
            mh_idx = i

adj = [l[mw_idx-1], l[(mw_idx+1)%6], l[mh_idx-1], l[(mh_idx+1)%6]]
m_area = 1
for i in l:
    if i not in adj:
        m_area *= i[1]
res = (mw*mh - m_area)*n
print(res)


"""
Method 1

추가 예시
7
1 60
4 30
2 160
3 50
1 100
4 20

"""

n = int(input())
w, h = [],[]
res = 0
direction = {i:0 for i in range(1,5)}

for i in range(6):
    d, l = map(int, input().split())
    direction[d] += 1
    if d == 1 or d == 2:
        w.append(l)
    elif d == 3 or d == 4:
        h.append(l)

widx = w.index(max(w))
hidx = h.index(max(h))
if direction[1] == 2 and direction[3] == 2:
    s = max(w) * max(h) - w[widx - 2] * h[hidx - 1]
elif direction[1] == 2 and direction[4] == 2:
    s = max(w) * max(h) - w[widx - 1] * h[hidx - 2]
elif direction[2] == 2 and direction[3] == 2:
    s = max(w) * max(h) - w[widx - 1] * h[hidx - 2]
elif direction[2] == 2 and direction[4] == 2:
    s = max(w) * max(h) - w[widx - 2] * h[hidx - 1]
print(s*n)




