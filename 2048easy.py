from copy import deepcopy

N=int(input())

board=[]
for _ in range(N):
    board.append(list(map(int, input().split(' '))))
#print(board)

def rotate(board):
    rst=[[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            rst[i][j]=board[N-j-1][i]

    return rst

answer=0
def dfs(now, n):
    global answer

    if n>5:
        return

    for _ in range(4):
        now=rotate(now)
        nxt=deepcopy(now)

        for x in range(N):
            for y1 in range(N):
                for y2 in range(y1+1, N):
                    if nxt[y2][x]==0:
                        continue

                    if nxt[y1][x]==0:
                        nxt[y1][x]+=nxt[y2][x]
                        nxt[y2][x]=0

                        continue

                    if nxt[y1][x]==nxt[y2][x]:
                        nxt[y1][x]+=nxt[y2][x]
                        nxt[y2][x]=0

                        break         

                    else:
                        break
        print(nxt)
        for y in range(N):
            answer=max(answer, max(nxt[y]))

        dfs(nxt, n+1)

dfs(board, 1)
print(answer)
    
