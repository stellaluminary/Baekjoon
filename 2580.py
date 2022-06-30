"""
Method 3

"""
import sys
s = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
blank = [(i,j) for i in range(9) for j in range(9) if s[i][j] == 0]

def check(x, y):
    num = [i for i in range(1, 10)]

    for i in range(9):
        if s[x][i] in num:
            num.remove(s[x][i])
        if s[i][y] in num:
            num.remove(s[i][y])

    nx, ny = x//3*3, y//3 *3
    for i in range(3):
        for j in range(3):
            if s[nx+i][ny+j] in num:
                num.remove(s[nx+i][ny+j])

    return num

def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*s[i])
        exit(0)

    x, y = blank[idx]
    candi = check(x, y)

    for c in candi:
        s[x][y] = c
        dfs(idx + 1)
        s[x][y] = 0

dfs(0)



"""
Method 2

python 3 28%
PyPy3
"""
import sys
s = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
blank = []

for i in range(9):
    for j in range(9):
        if s[i][j] == 0:
            blank.append((i,j))

def row_ck(x, a):
    for i in range(9):
        if a == s[x][i]:
            return False
    return True

def col_ck(y, a):
    for i in range(9):
        if a == s[i][y]:
            return False
    return True

def sq_ck(x, y, a):
    nx, ny = x//3 * 3, y//3*3
    for i in range(3):
        for j in range(3):
            if a == s[nx+i][ny+j]:
                return False
    return True

def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*s[i])
        exit(0)

    for i in range(1, 10):
        x, y = blank[idx]

        if row_ck(x, i) and col_ck(y, i) and sq_ck(x, y, i):
            s[x][y] = i
            dfs(idx+1)
            s[x][y]=  0

dfs(0)


"""
Method 1

Python3, PyPy3(12%) 모두 시간초과
"""

def row_ck(x):
    row = [0]*10
    zero = []

    for i in s[x]:
        if i != 0:
            row[i]=1

    for i in range(1, 10):
        if row[i] == 0:
            zero.append(i)

    return zero

def col_ck(y):
    col = [0]*10
    zero = []

    for i in range(9):
        if s[i][y] != 0:
            col[s[i][y]]=1

    for i in range(1, 10):
        if col[i] == 0:
            zero.append(i)

    return zero

def sq_ck(x,y):
    sq = [0]*10
    zero = []

    a, b = x%3, y%3

    for i in range(3):
        for j in range(3):
            if a == 0:
                if b == 0 and s[x+i][y+j] != 0:
                    sq[s[x+i][y+j]] = 1
                elif b == 1 and s[x+i][y+1-j] != 0:
                    sq[s[x+i][y+1-j]] = 1
                elif b == 2 and s[x+i][y-j] != 0:
                    sq[s[x+i][y-j]] = 1
            elif a == 1:
                if b == 0 and s[x+1-i][y+j] != 0:
                    sq[s[x+1-i][y+j]] = 1
                elif b == 1 and s[x+1-i][y+1-j] != 0:
                    sq[s[x+1-i][y+1-j]] = 1
                elif b == 2 and s[x+1-i][y-j] != 0:
                    sq[s[x+1-i][y-j]] = 1
            elif a == 2:
                if b == 0 and s[x-i][y+j] != 0:
                    sq[s[x-i][y+j]] = 1
                elif b == 1 and s[x-i][y+1-j] != 0:
                    sq[s[x-i][y+1-j]] = 1
                elif b == 2 and s[x-i][y-j] != 0:
                    sq[s[x-i][y-j]] = 1

    for i in range(1, 10):
        if sq[i] == 0:
            zero.append(i)

    return zero

def dfs(idx):
    if idx == len(loc):
        res.append(copy.deepcopy(s))
        return

    x, y = loc[idx]
    c = []
    for i in row_ck(x):
        for j in col_ck(y):
            for k in sq_ck(x,y):
                if i == j == k:
                    c.append(i)

    for i in c:
        s[x][y] = i
        dfs(idx+1)
        s[x][y] = 0

import sys
import copy
s = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
visit = [[0]*9 for _ in range(9)]
loc = []
res = []

for i in range(9):
    for j in range(9):
        if not s[i][j]:
            loc.append((i,j))
dfs(0)
for i in res[0]:
    print(' '.join(map(str, i)))



"""
예제 1
입력
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0
출력
1 3 5 4 6 9 2 7 8
7 8 2 1 3 5 6 4 9
4 6 9 2 7 8 1 3 5
3 2 1 5 4 6 8 9 7
8 7 4 9 1 3 5 2 6
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 4 3 7 8 1 9 5 2
2 5 8 3 9 4 7 6 1

예제 2
입력
0 0 0 0 0 0 0 0 0
7 8 2 1 3 5 6 4 9
4 6 9 2 7 8 1 3 5
3 2 1 5 4 6 8 9 7
0 0 0 0 0 0 0 0 0
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 4 3 7 8 1 9 5 2
0 0 0 0 0 0 0 0 0
출력
1 3 5 4 6 9 2 7 8 
7 8 2 1 3 5 6 4 9 
4 6 9 2 7 8 1 3 5 
3 2 1 5 4 6 8 9 7 
8 7 4 9 1 3 5 2 6 
5 9 6 8 2 7 4 1 3 
9 1 7 6 5 2 3 8 4 
6 4 3 7 8 1 9 5 2 
2 5 8 3 9 4 7 6 1 

"""




