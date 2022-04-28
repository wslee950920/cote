from collections import deque

N, L, R=map(int, input().split(' '))

land=[]
for _ in range(N):
    land.append(list(map(int, input().split(' '))))

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

answer=0
while True:
    unions=[]
    visited=[[False]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            #print(i, j, visited)
            if visited[i][j]:
                continue

            union=[]
            union.append([i, j])

            q=deque()
            q.append([i, j])

            while q:
                x, y=q.popleft()

                for k in range(4):
                    nx=x+dx[k]
                    ny=y+dy[k]

                    if nx<0 or nx>=N or ny<0 or ny>=N:
                        continue

                    diff=abs(land[nx][ny]-land[x][y])
                    if L<=diff<=R and [nx, ny] not in union:
                        union.append([nx, ny])

                        q.append([nx, ny])

            #print('union', union)
            if len(union)>1:
                unions.append(union)

                for x, y in union:
                    visited[x][y]=True

    #print('unions', unions)
    if not unions:
        break

    else:
        answer+=1

        for union in unions:
            tot=0
            for x, y in union:
                tot+=land[x][y]

            rst=tot//len(union)
            for x, y in union:
                land[x][y]=rst
        #print('land', land)

print(answer)