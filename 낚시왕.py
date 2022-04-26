R, C, M=map(int, input().split(' '))

data=[]
for _ in range(M):
    data.append(list(map(int, input().split(' '))))
#print(data)

dc=[0, 0, 0, 1, -1]
dr=[0, -1, 1, 0, 0]

board=[[0]*(C+1) for _ in range(R+1)]
for r, c, _, _, z in data:
    board[r][c]=z
#print(board)

answer=0
for x in range(1, C+1):
    y=0
    while y<R+1:
        if board[y][x]!=0:
            answer+=board[y][x]
            board[y][x]=0

            break

        y+=1

    tmp=[]
    for r, c, s, d, _ in data:
        #print(r, c, s, d, board[r][c])

        nr=r
        nc=c
        nd=d

        if board[r][c]==0:
            continue

        z=board[r][c]

        for _ in range(s):
            if nd==1 or nd==2:
                if nr==1:
                    nd=2

                elif nr==R:
                    nd=1
            
            elif nd==3 or nd==4:
                if nc==1:
                    nd=3

                elif nc==C:
                    nd=4

            nr+=dr[nd]
            nc+=dc[nd]

        board[r][c]=0
        board[nr][nc]=max(board[nr][nc], z)
        #print(answer, board)

        tmp.append([nr, nc, s, nd, None])
    data=tmp

print(answer)