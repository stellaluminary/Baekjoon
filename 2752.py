"""
Method 2

"""

print(*sorted(map(int,input().split())))

"""
Method 1

"""
print(' '.join(map(str, sorted(list(map(int, input().split()))))))