from collections import deque

N=int(input())

sea=[]
shark=None
sz=2

for i in range(N):
    sea.append(list(map(int, input().split(' '))))

    for j in range(N):
        if sea[i][j]==9:
            shark=[i, j]

            sea[i][j]=0

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

answer=0
m=0

while True:
    visited=[[False]*N for _ in range(N)]
    visited[shark[0]][shark[1]]=True

    fishes=[]
    dist=N*N+1

    q=deque()
    q.append(shark+[0])

    while q:
        x, y, n=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue

            if visited[nx][ny]:
                continue

            if sea[nx][ny]<=sz:
                visited[nx][ny]=True

                if 0<sea[nx][ny]<sz:
                    if n+1>dist:
                        break

                    else:
                        dist=n+1

                    fishes.append([nx, ny])

                q.append([nx, ny, n+1])

        else:
            continue

        break

    if not fishes:
        break

    else:
        answer+=dist

        fishes.sort()
        #print(shark, 'fishes', fishes)

        i, j=fishes[0]
        shark=[i, j]
        sea[i][j]=0
        m+=1

        if m==sz:
            sz+=1

            m=0

    #print('shark', shark)
    #print('sea', sea)
    #print('m', m, 'size', sz)
    #print('answer', answer)
    
print(answer)   