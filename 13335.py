"""
Method 2

"""
from collections import deque

n,w,l = map(int, input().split())
trucks = deque(list(map(int, input().split())))
bridge = deque([0]*w)
time = 0

while trucks:
    bridge.popleft()
    if len(bridge) < w:
        if sum(bridge) + trucks[0] <= l:
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)
    time += 1
time += w
print(time)


"""
Method 1
시간 초과
"""

n,w,l = map(int, input().split())
arr = list(map(int, input().split()))

# 다리 위에 올라간 트럭
onB = []
# 현재 시간
time = 0
# 현재의 다리에 올라간 무게 load
load = 0

for idx, a in enumerate(arr):
    if l >= load + arr[idx]:
        time += 1
        onB.append((arr[idx], time))
        load += arr[idx]
    else:
        while l < load + arr[idx]:
            if time == onB[0][1] + w:
                load -= onB[0][0]
                onB.pop(0)
            else:
                time += 1

        onB.append((arr[idx], time))
        load += arr[idx]

time = onB[-1][1] + w
print(time)










