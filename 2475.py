"""
Method 1

"""
import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
s = [i**2 for i in a]
print(sum(s)%10)









