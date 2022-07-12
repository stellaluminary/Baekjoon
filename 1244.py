"""
Method 3

"""

"""
Method 2

"""
n = int(input())
switch = [0] + list(map(int, input().split()))

rev = {0:1, 1:0}

for _ in range(int(input())):
    s, g = map(int, input().split())

    if s == 1:
        for j in range(g, n+1, g):
            switch[j] = rev[switch[j]]
    else:
        switch[g] = rev[switch[g]]
        i = 1
        while (g-i >= 1) and (g+i <= n) and (switch[g-i] == switch[g+i]):
            switch[g-i], switch[g+i] = rev[switch[g-i]], rev[switch[g+i]]
            i += 1

for e, v in enumerate(switch[1:], start=1):
    print(v, end=' ')
    if e % 20 == 0:
        print()



"""
Method 1


또 다른 예제 
50
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1
2
1 3
2 3

결과
1 0 0 0 1 0 0 1 1 1 0 0 0 1 1 1 0 0 0 1
1 1 0 0 0 1 1 1 0 0 0 1 1 1 0 0 0 1 1 1
0 0 0 1 1 1 0 0 0 1
"""

n = int(input())
switch = [0] + list(map(int, input().split()))

for i in range(int(input())):
    s, g = map(int, input().split())

    if s == 1:
        for j in range(1, len(switch)):
            if j % g == 0:
                switch[j] = 1 if switch[j] == 0 else 0
    else:
        switch[g] = 1 if switch[g] == 0 else 0
        for j in range(1, len(switch)-g):
            if g-j < 1:
                break
            if switch[g-j] == switch[g+j]:
                switch[g-j] = 1 if switch[g-j] == 0 else 0
                switch[g+j] = 1 if switch[g+j] == 0 else 0
            else:
                break

twenty = (len(switch)-1) // 20
for i in range(twenty+1):
    if i == twenty:
        val = switch[20*i + 1:]
    else:
        val = switch[20*i + 1:20*(i+1)+1]
    print(' '.join(map(str, val)))
