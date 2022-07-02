"""
Method 1

"""

import sys
input = sys.stdin.readline

n = list(input().rstrip())
n.sort(reverse=True)
print(''.join(n))


