N, M, K=map(int, input().split(' '))

land=[[5]*N for _ in range(N)]

A=[]
for _ in range(N):
    A.append(list(map(int, input().split(' '))))

info=[]
for _ in range(M):
    x, y, z=list(map(int, input().split(' ')))

    info.append([x-1, y-1, z])

tree=[[[] for _ in range(N)] for _ in range(N)]
for x, y, z in info:
    tree[x][y].append(z)
    tree[x][y].sort()

#print('initial', tree, land)

dx=[-1, 1, 0, 0, -1, -1, 1, 1]
dy=[0, 0, -1, 1, -1, 1, -1, 1]

for _ in range(K):
    for s in range(3):
        for x in range(N):
            for y in range(N):
                if s==0:
                    if not tree[x][y]:
                        continue
                    tree[x][y].sort()

                    i=0
                    while i<len(tree[x][y]) and land[x][y]-tree[x][y][i]>=0:
                        land[x][y]-=tree[x][y][i]
                        tree[x][y][i]+=1

                        i+=1

                    while tree[x][y][i:]:
                        land[x][y]+=tree[x][y].pop()//2

                elif s==1:
                    for t in tree[x][y]:
                        if t%5==0:
                            for j in range(8):
                                nx=x+dx[j]
                                ny=y+dy[j]

                                if nx<0 or nx>=N or ny<0 or ny>=N:
                                    continue

                                tree[nx][ny].append(1)

                elif s==2:
                    land[x][y]+=A[x][y]

                #print(s, x, y)
                #print('tree', tree)
                #print('land', land)

#print('rst', tree)
answer=0
for i in range(N):
    for j in range(N):
        answer+=len(tree[i][j])
print(answer)