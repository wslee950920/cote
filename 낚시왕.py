R, C, M=map(int, input().split(' '))

board=[[[] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r, c, s, d, z=map(int, input().split(' '))

    board[r-1][c-1].append([z, s, d-1])
#print(board)

dx=[-1, 1, 0, 0]
dy=[0, 0, 1, -1]

answer=0

for land in range(C):
    print(land)

    depth=0
    while depth<R:
        if board[depth][land]:
            z, _, _=board[depth][land].pop()
            answer+=z

            break

        depth+=1

    tmp=[[[] for _ in range(C)] for _ in range(R)]

    for x in range(R):
        for y in range(C):
            if not board[x][y]:
                continue
                
            z, s, d=board[x][y].pop()
            print('before', x, y, d, z)

            nx=x+dx[d]*s
            ny=y+dy[d]*s

            if nx<0 or nx>=R or ny<0 or ny>=C:
                if d==0 or d==1:
                    c=R*2-2

                    nx=abs(nx)%c
                    if nx>=R:
                        nx=c-nx

                        if d==1:
                            d=0

                    else:
                        if d==0:
                            d=1

                elif d==2 or d==3:
                    c=C*2-2

                    ny=abs(ny)%c
                    if ny>=C:
                        ny=c-ny

                        if d==2:
                            d=3

                    else:
                        if d==3:
                            d=2                   

            print('after', nx, ny, d, z)
            tmp[nx][ny].append([z, s, d])
    print('tmp', tmp)

    for i in range(R):
        for j in range(C):
            if tmp[i][j]:
                tmp[i][j].sort(reverse=True)

                board[i][j].append(tmp[i][j][0])
    print('rst', board)
print(answer)