N, M=map(int, input().split(' '))
r, c, d=map(int, input().split(' '))
board=[]
for _ in range(N):
    board.append(list(map(int, input().split(' '))))

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

answer=1
board[r][c]=2

def dfs(now):
    global answer

    x, y, d=now

    for n in range(1, 5):
        nd=(d-n+4)%4
        nx=x+dx[nd]
        ny=y+dy[nd]

        if board[nx][ny]==0:
            board[nx][ny]=2

            answer+=1

            dfs([nx, ny, nd])

    else:
        nx=x-dx[d]
        ny=y-dy[d]

        if board[nx][ny]==1:
            print(answer)

            exit()

        else:
            dfs([nx, ny, d])
dfs([r, c, d])