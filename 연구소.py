from itertools import combinations
from copy import deepcopy
from collections import deque

N, M=map(int, input().split(' '))

board=[]
for _ in range(N):
    board.append(list(map(int, input().split(' '))))
#print(board)

blks=[]
virs=[]
walls=0
for i in range(N):
    for j in range(M):
        if board[i][j]==0:
            blks.append([i, j])

        if board[i][j]==1:
            walls+=1

        if board[i][j]==2:
            virs.append([i, j])

combs=list(combinations(blks, 3))
#print(combs)

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

answer=0

for adds in combs:
    #print(walls)

    copied=deepcopy(board)
    for x, y in adds:
        copied[x][y]=1

    q=deque()

    for vir in virs:
        copied[vir[0]][vir[1]]=2

        q.append(vir)

    while q:
        x, y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue

            if copied[nx][ny]==0:
                copied[nx][ny]=2

                q.append([nx, ny])

    plt=0
    for i in range(N):
        plt+=copied[i].count(2)

    answer=max(answer, N*M-3-walls-plt)
print(answer)

