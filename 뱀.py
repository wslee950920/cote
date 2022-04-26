from collections import deque

N=int(input())
board=[[0]*N for _ in range(N)]
board[0][0]=1

K=int(input())
for _ in range(K):
    y, x=map(int, input().split(' '))
    board[y-1][x-1]=2
#print(board)

L=int(input())
#print(L)

dir=[]
for _ in range(L):
    X, C=input().split(' ')

    dir.append([int(X), C])
dir.append([10000, None])
#print(dir)

dx=[0, 0, -1, 1]
dy=[-1, 1, 0, 0]

def solution(board):
    snake=deque()
    snake.append([0, 0])
    i=3

    t=0
    for X, C in dir:
        while t<X:
            t+=1

            head=snake[0]
            ny=head[0]+dy[i]
            nx=head[1]+dx[i]

            if ny<0 or ny>=N or nx<0 or nx>=N:
                return t

            if board[ny][nx]==1:
                return t

            if board[ny][nx]==0:
                board[ny][nx]=1
                snake.appendleft([ny, nx])

                tail=snake.pop()
                board[tail[0]][tail[1]]=0

            elif board[ny][nx]==2:
                board[ny][nx]=1
                snake.appendleft([ny, nx])

            print(t)
            print(board)

        if i==0:
            if C=='L':
                i=2

            elif C=='D':
                i=3

        elif i==1:
            if C=='L':
                i=3

            elif C=='D':
                i=2

        elif i==2:
            if C=='L':
                i=1

            elif C=='D':
                i=0

        elif i==3:
            if C=='L':
                i=0

            elif C=='D':
                i=1

print(solution(board))