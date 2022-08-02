"""
Method 1

"""
import sys
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(n)]
    score.sort()
    min_r = score[0][1]
    cnt = 1

    for i in range(1, n):
        if score[i][1] < min_r:
            cnt += 1
            min_r = score[i][1]
    print(cnt)










