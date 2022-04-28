from itertools import combinations
import math

N, M=map(int, input().split(' '))

mp=[]
for _ in range(N):
    mp.append(list(map(int, input().split(' '))))

hous=[]
chcks=[]
for i in range(N):
    for j in range(N):
        if mp[i][j]==1:
            hous.append([i, j])

        elif mp[i][j]==2:
            chcks.append([i, j])

answer=math.inf

for cbnt in list(combinations(chcks, M)):
    print(cbnt)

    tot=0
    for r1, c1 in hous:
        rst=math.inf

        for r2, c2 in cbnt:
            rst=min(rst, abs(r1-r2)+abs(c1-c2))

        print(rst)
        tot+=rst
        if tot>answer:
            break

    else:
        print(tot, answer)
        answer=min(answer, tot)
print(answer)
