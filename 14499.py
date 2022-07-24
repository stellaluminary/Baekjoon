"""
Method 2

"""
n,m,x,y,k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
action = list(map(int, input().split()))
dice = [0]*6

def turn(dir):
    if dir == 1:
        dice[0],dice[2],dice[3],dice[5] = dice[3],dice[0],dice[5],dice[2]
    elif dir == 2:
        dice[0],dice[2],dice[3],dice[5] = dice[2],dice[5],dice[0],dice[3]
    elif dir == 3:
        dice[0],dice[1],dice[4],dice[5] = dice[4],dice[0],dice[5],dice[1]
    elif dir == 4:
        dice[0],dice[1],dice[4],dice[5] = dice[1],dice[5],dice[0],dice[4]

move = [(0,0),(0,1),(0,-1),(-1,0),(1,0)]

for i in range(k):
    nx, ny = x + move[action[i]][0], y + move[action[i]][1]
    if 0 <= nx < n and 0 <= ny < m:
        x, y = nx, ny
        turn(action[i])
        if graph[x][y]:
            dice[5] = graph[x][y]
            graph[x][y] = 0
        else:
            graph[x][y] = dice[5]
        print(dice[0])





"""
Method 1

"""

n,m,x,y,k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
action = list(map(int, input().split()))

move = {1:(0,1), 2:(0,-1), 3:(-1,0), 4:(1,0)}
horizontal = [0]*4
vertical = [0]*4
for i in range(len(action)):
    if action[i] in [1,2]:
        nx, ny = x + move[action[i]][0], y + move[action[i]][1]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        else:
            x, y = nx, ny

        horizontal[1], horizontal[3] = vertical[1], vertical[3]
        if action[i] == 1:
            horizontal = horizontal[1:] + [horizontal[0]]
        else:
            horizontal = [horizontal[-1]] + horizontal[:-1]

        if graph[x][y]:
            horizontal[-1] = graph[x][y]
            graph[x][y] = 0
        else:
            graph[x][y] = horizontal[-1]
        vertical[1], vertical[3] = horizontal[1], horizontal[3]
        #print(horizontal[1])
    else:
        nx, ny = x + move[action[i]][0], y + move[action[i]][1]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        else:
            x, y = nx, ny

        vertical[1], vertical[3] = horizontal[1], horizontal[3]
        if action[i] == 3:
            vertical = vertical[1:] + [vertical[0]]
        else:
            vertical = [vertical[-1]] + vertical[:-1]

        if graph[x][y]:
            vertical[-1] = graph[x][y]
            graph[x][y] = 0
        else:
            graph[x][y] = vertical[-1]
        horizontal[1], horizontal[3] = vertical[1], vertical[3]
        #print(vertical[1])
    print(action[i], vertical, horizontal)

























