R, C, T=map(int, input().split(' '))

cln=[]
A=[]
for i in range(R):
    A.append(list(map(int, input().split(' '))))

    for j in range(C):
        if A[i][j]==-1:
            cln.append([i, j])

            A[i][j]=0
#print(cln)

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

for _ in range(T):
    tmp=[[0]*C for _ in range(R)]

    for x in range(R):
        for y in range(C):
            if A[x][y]>0:
                #print(x, y)

                n=0

                for i in range(4):
                    nx=x+dx[i]
                    ny=y+dy[i]

                    if nx<0 or nx>=R or ny<0 or ny>=C:
                        continue

                    if [nx, ny] in cln:
                        continue

                    tmp[nx][ny]+=A[x][y]//5
                    n+=1

                A[x][y]-=(A[x][y]//5)*n
                #print('A', A)
                #print('tmp', tmp)

    for i in range(R):
        for j in range(C):
            A[i][j]+=tmp[i][j]
    #print('dirt', A)

    for i in range(len(cln)):
        x, y=cln[i]
        
        nx=x
        ny=y

        if i==0:
            while nx+dx[0]>=0:
                A[nx][ny], A[nx+dx[0]][y]=A[nx+dx[0]][ny], A[nx][ny]

                nx+=dx[0]

        elif i==1:
            while nx+dx[1]<R:
                A[nx][ny], A[nx+dx[1]][y]=A[nx+dx[1]][ny], A[nx][ny]

                nx+=dx[1]
        #print(nx, ny, A)

        while ny+dy[3]<C:
            A[nx][ny], A[nx][ny+dy[3]]=A[nx][ny+dy[3]], A[nx][ny]

            ny+=dy[3]
        #print(nx, ny, A)

        if i==0:
            while nx+dx[1]<=x:
                A[nx][ny], A[nx+dx[1]][ny]=A[nx+dx[1]][ny], A[nx][ny]

                nx+=dx[1]

        elif i==1:
            while nx+dx[0]>=x:
                A[nx][ny], A[nx+dx[0]][ny]=A[nx+dx[0]][ny], A[nx][ny]

                nx+=dx[0]
        #print(nx, ny, A)

        while ny+dy[2]>0:
            A[nx][ny], A[nx][ny+dy[2]]=A[nx][ny+dy[2]], A[nx][ny]

            ny+=dy[2]

        #print([nx, ny], [x, y], A[x][y], A)
        A[x][y]=0
    #print('tmp', tmp)
    #print('rst', A)

answer=0
for i in range(R):
    for j in range(C):
        answer+=A[i][j]
print(answer)