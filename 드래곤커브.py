from copy import deepcopy

N=int(input())

info=[]
for _ in range(N):
    info.append(list(map(int, input().split(' '))))

dy=[0, -1, 0, 1]
dx=[1, 0, -1, 0]

M=101
board=[[0]*M for _ in range(M)]
dragon=[]

def rotate(base, y1, x1, y2, x2):
    rst=[[0]*M for _ in range(M)]
    
    ny1=None
    nx1=None
    ny2=None
    nx2=None

    for i in range(M):
        for j in range(M):
            if i==y1 and j==x1:
                ny1=j
                nx1=M-1-i

            if i==y2 and j==x2:
                ny2=j
                nx2=M-1-i

            rst[j][M-1-i]=base[i][j]

    return rst, ny1, nx1, ny2, nx2

def dfs(now, y1, x1, y2, x2, gen):
    global dragon

    #print(now, [y1, x1], [y2, x2], gen)

    if gen==0:
        for i in range(M):
            for j in range(M):
                if now[i][j]==1:
                    dragon.append([i, j])

        return

    nxt, ny1, nx1, ny2, nx2=rotate(deepcopy(now), y1, x1, y2, x2)
    #print(nxt, [ny1, nx1], [ny2, nx2])
    dy=ny2-y2
    dx=nx2-x2
    #print(dy, dx)

    for i in range(M):
        for j in range(M):
            if nxt[i][j]==1:
                now[i-dy][j-dx]=nxt[i][j]

    dfs(now, y1, x1, ny1-dy, nx1-dx, gen-1)

for x, y, d, g in info:
    ny=y+dy[d]
    nx=x+dx[d]

    copied=deepcopy(board)
    copied[y][x]=1
    copied[ny][nx]=1

    dfs(copied, y, x, ny, nx, g)

for y, x in dragon:
    board[y][x]=1
#print(board)

answer=0
for y in range(M-1):
    for x in range(M-1):
        if board[y][x]==1 and board[y][x+1]==1 and board[y+1][x]==1 and board[y+1][x+1]==1:
            answer+=1
print(answer)