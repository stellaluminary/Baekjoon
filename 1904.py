# 피보나치로 문제 해결

"""
메모리 초과
n < 1백만
def t(n):
    if n == 1:
        return '1'

    l=['00','1']
    b = True
    while b:
        p = []
        k=0
        for i in l:
            if n-len(i) >= 2:
                p.append(i + '00')
                p.append(i + '1')
            elif n-len(i) == 1:
                p.append(i + '1')
            elif n-len(i) == 0:
                k += 1
                p.append(i)

        if k == len(l):
            b = False
        l=p
    return len(l)

n = int(input())
print(int(t(n)) % 15746)
"""