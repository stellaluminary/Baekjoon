"""
Method 4

"""

def cal():
    tmp = 0
    for hx, hy in house: # 1에 위치하는 모든 house를 하나씩 뽑아 치킨 거리를 구함
        dist = 1e9
        for e, (cx, cy) in t_ch: # 2에 위치한 치킨집과 특정 house와의 치킨 거리 구함.
            dist = min(dist, abs(hx - cx) + abs(hy - cy))
        tmp += dist
    res.append(tmp)

def select_chicken(cnt):
    # 백트래킹의 조건으로 m과 숫자가 일치할 때 치킨 거리를 구해 res 리스트에 저장
    if cnt == m:
        cal()
        return

    for e, (cx, cy) in enumerate(chick):
        if visit[cx][cy] == 0: # 특정 치킨 집을 방문했는지 처리함.
            if t_ch: # 시간 단축과 오름차순의 조합이 가능하도록 하기 위해 배치
                if e < t_ch[-1][0]:
                    continue

            visit[cx][cy] = 1 # 특정 치킨집 방문 처리
            t_ch.append((e, (cx,cy)))
            select_chicken(cnt + 1)
            visit[cx][cy] = 0 # 특정 치킨집 방문 철회
            t_ch.pop()

n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
house = []
chick = []
visit = [[0]*(n) for _ in range(n)]
t_ch = []
res = []
for i in range(n):
    for j in range(n):
        if l[i][j] == 1:
            house.append((i,j))
        elif l[i][j] == 2:
            chick.append((i,j))

select_chicken(0)
print(min(res))


"""
Method 3
"""

from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l=[list(map(int, input().split())) for _ in range(n)]
house = []
chick = []
for i in range(n):
    for j in range(n):
        if l[i][j] == 1:
            house.append((i,j))
        elif l[i][j] == 2:
            chick.append((i,j))

res = 1e9
for ch in combinations(chick, m):
    tmp = 0
    for hx, hy in house:
        mini = 1e9
        for cx, cy in ch:
            mini = min(mini, abs(hx - cx) + abs(hy - cy))
        tmp += mini
    res = min(res, tmp)
print(res)




"""
Method 2
Method 1 수정 버전
"""

from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l=[]
for i in range(n):
    l.append(list(map(int, input().split())))
o_loc = []
s_loc = []
for i in range(n):
    for j in range(n):
        if l[i][j] == 1:
            o_loc.append((i,j))
        elif l[i][j] == 2:
            s_loc.append((i,j))

t = combinations(s_loc, m)

def cal_sec(combi):
    sec_res = 0
    for one in o_loc:
        ox, oy = one
        mini = 1e9
        for sec in combi:
            sx, sy = sec
            mini = min(mini, abs(sx - ox) + abs(sy - oy))
        sec_res += mini
    return sec_res

mini = 1e9
for i in t:
    mini = min(mini, cal_sec(i))
print(mini)

"""
Method 1
초기 시도
"""

import copy
from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l=[]
for i in range(n):
    l.append(list(map(int, input().split())))
b = [[0]*n for _ in range(n)]
o_loc = []
s_loc = []
for i in range(n):
    for j in range(n):
        if l[i][j] == 1:
            o_loc.append((i,j))
            b[i][j] = 1
        elif l[i][j] == 2:
            s_loc.append((i,j))

t = list(combinations(s_loc, m))

def cal_sec(combi):
    table = copy.deepcopy(b)
    for sx, sy in combi:
        table[sx][sy] = 2
    sec_res = []
    for one in o_loc:
        ox, oy = one
        mini = 1e9
        for sec in combi:
            sx, sy = sec
            res = abs(sx - ox) + abs(sy - oy)
            if mini > res:
                mini = res
        sec_res.append(mini)
    return sum(sec_res)

mini = 1e9
for i in t:
    tmp = cal_sec(i)
    if tmp < mini:
        mini = tmp
print(mini)