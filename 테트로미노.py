N, M=map(int, input().split(' '))

paper=[]
mx=0
for _ in range(N):
    lst=list(map(int, input().split(' ')))

    mx=max(mx, max(lst))
    paper.append(lst)

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

answer=0
checked=[]

def dfs(now, idx, tot):
    global answer, checked

    if len(now)==3 and tot+mx<answer:
        return

    if len(now)==4:
        print(now)

        answer=max(answer, tot)
        print(answer)

        return

    x, y=now[idx]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue

        if [nx, ny] in now:
            continue

        nxt=now+[[nx, ny]]
        if len(nxt)==3:
            dfs(nxt, idx, tot+paper[nx][ny])

        dfs(nxt, idx+1, tot+paper[nx][ny])       

for x in range(N):
    for y in range(M):
        dfs([[x, y]], 0, paper[x][y])

print(answer)