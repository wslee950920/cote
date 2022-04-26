from collections import deque

gears=[None]
for _ in range(4):
    gears.append(deque(list(map(int, list(input())))))

K=int(input())

ways=[]
for _ in range(K):
    ways.append(list(map(int, input().split(' '))))

def left_dfs(now, dir):
    global gears

    if now>1 and gears[now-1][2]!=gears[now][6]:
        left_dfs(now-1, -dir)

        if dir==1:
            gears[now-1].append(gears[now-1].popleft())

        elif dir==-1:
            gears[now-1].appendleft(gears[now-1].pop())

def right_dfs(now, dir):
    global gears

    if now<4 and gears[now][2]!=gears[now+1][6]:
        right_dfs(now+1, -dir)

        if dir==1:
            gears[now+1].append(gears[now+1].popleft())

        elif dir==-1:
            gears[now+1].appendleft(gears[now+1].pop())

for num, dir in ways:
    left_dfs(num, dir)
    right_dfs(num, dir)

    if dir==-1:
        gears[num].append(gears[num].popleft())

    elif dir==1:
        gears[num].appendleft(gears[num].pop())
    
    #print('rst', gears)

answer=0
for i in range(4):
    if gears[i+1][0]==1:
        answer+=2**i
print(answer)