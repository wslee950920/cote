from collections import deque

N, M=map(int, input().split(' '))

board=[]
for _ in range(N):
    board.append(list(input()))
#print(board)

def findRB(board):
    rst=dict()

    for i in range(N):
        for j in range(M):
            if board[i][j]=='R':
                rst['R']=[i, j]

                board[i][j]='.'

            if board[i][j]=='B':
                rst['B']=[i, j]

                board[i][j]='.'

            if len(rst.keys())==2:
                return rst['R'], rst['B']

def solution(board):
    dx=[0, 0, -1, 1]
    dy=[-1, 1, 0, 0]

    red, blue=findRB(board)

    q=deque()
    q.append([red, blue, 1])

    while q:
        [[ry, rx], [by, bx], n]=q.popleft()
        #print('f', ry, rx, by, bx, n)
        
        for i in range(4):
            r=0
            nry=ry
            nrx=rx
            while board[nry+dy[i]][nrx+dx[i]]!='#':
                r+=1

                nry+=dy[i]
                nrx+=dx[i]

                if board[nry][nrx]=='O':
                    break

            b=0
            nby=by
            nbx=bx
            while board[nby+dy[i]][nbx+dx[i]]!='#':
                b+=1

                nby+=dy[i]
                nbx+=dx[i]

                if board[nby][nbx]=='O':
                    break

            if board[nby][nbx]=='O':
                continue

            if board[nry][nrx]=='O':
                return n

            if nry==nby and nrx==nbx:
                if r>b:
                    nry-=dy[i]
                    nrx-=dx[i]

                else:
                    nby-=dy[i]
                    nbx-=dx[i]

            if n+1>10:
                continue

            #print('s', i, nry, nrx, nby, nbx, n+1)
            q.append([[nry, nrx], [nby, nbx], n+1])

    return -1
print(solution(board))

