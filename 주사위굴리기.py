N, M, x, y, K=map(int, input().split(' '))
board=[]
for _ in range(N):
    board.append(list(map(int, input().split(' '))))
#print(board)
cmd=list(map(int, input().split(' ')))
#print(cmd)

dx=[0, 0, 0, -1, 1]
dy=[0, 1, -1, 0, 0]

dice=[0]*(6+1)
for i in cmd:
    if x+dx[i]<0 or x+dx[i]>=N or y+dy[i]<0 or y+dy[i]>=M:
        continue

    x+=dx[i]
    y+=dy[i]
    #print(i, y, x)

    if i==1:
        dice[1], dice[3], dice[6], dice[4]=dice[4], dice[1], dice[3], dice[6]

    elif i==2:
        dice[1], dice[4], dice[3], dice[6]=dice[3], dice[1], dice[6], dice[4]

    elif i==3:
        dice[1], dice[5], dice[2], dice[6]=dice[5], dice[6], dice[1], dice[2]

    elif i==4:
        dice[1], dice[6], dice[2], dice[5]=dice[2], dice[5], dice[6], dice[1]

    if board[x][y]==0:
        board[x][y]=dice[6]

    else:
        dice[6]=board[x][y]
        board[x][y]=0
    #print(board, dice)

    #print('top', dice[1], 'bottom', dice[6])
    print(dice[1])


