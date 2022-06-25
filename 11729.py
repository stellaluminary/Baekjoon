"""
Method 1

"""

def hanoi(n, src, dst):
    tmp = 6 - src - dst
    if n == 0:
        return
    hanoi(n-1, src, tmp)
    print(src, dst)
    hanoi(n-1, tmp, dst)

n = int(input())
print(2**n - 1)
hanoi(n, 1, 3)

"""
Method 2

"""

N = int(input())
def h(n,f,b,t):
    if n==1:print(f,t)
    else:
        h(n-1,f,t,b)
        print(f,t)
        h(n-1,b,f,t)
print(2**N-1)
h(N,1,2,3)














