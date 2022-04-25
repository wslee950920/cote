from copy import deepcopy

N, M=map(int, input().split(' '))

room=[]
for _ in range(N):
    room.append(list(map(int, input().split(' '))))

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

dirs=[None, [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 3], [3, 1], [2, 1], [0, 2]], [[0, 2, 3], [0, 3, 1], [2, 3, 1], [0, 2, 1]], [[0, 1, 2, 3]]]

cctv=[]
for i in range(N):
    for j in range(M):
        if room[i][j] in [n for n in range(1, 6)]:
            cctv.append([i, j])

answer=N*M+1

def dfs(idx, now):
    global answer

    if idx==len(cctv):
        print(now)

        rst=0
        for row in now:
            rst+=row.count(0)
        
        answer=min(answer, rst)

        return

    x, y=cctv[idx]
    num=room[x][y]

    for dir in dirs[num]:
        nxt=deepcopy(now)

        for i in dir:
            nx=x+dx[i]
            ny=y+dy[i]

            while nx>=0 and nx<N and ny>=0 and ny<M:
                if nxt[nx][ny]==6:
                    break

                elif nxt[nx][ny]==0:
                    nxt[nx][ny]='#'

                nx+=dx[i]
                ny+=dy[i]

        dfs(idx+1, nxt)

dfs(0, room)
print(answer)




    