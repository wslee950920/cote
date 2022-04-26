from audioop import reverse
from functools import reduce

N, L=map(int, input().split(' '))

mp=[]
for _ in range(N):
    mp.append(list(map(int, input().split(' '))))

answer=0
cols=list(zip(*mp))

for a in range(N):
    row=mp[a]
    col=cols[a]
    #print(row, col)

    slopes=[]
    for b in range(len(row)-1):
        c=b+1

        if row[b]!=row[c]:
            if row[b]<row[c]:
                if c-L<0:
                   break

                tmp=[]
                for d in range(c-L, c):
                    if [a, d] in slopes or row[c]-1!=row[d]:
                        break

                    tmp.append([a, d])

                else:
                    slopes+=tmp

                    continue

                break

            elif row[b]>row[c]:
                if b+L>=N:
                    break

                tmp=[]
                for d in range(b+1, b+L+1):
                    if [a, d] in slopes or row[b]-1!=row[d]:
                        break

                    tmp.append([a, d])

                else:
                    slopes+=tmp

                    continue

                break

    else:
        print(row)

        answer+=1

    slopes=[]
    for b in range(len(col)-1):
        c=b+1

        if col[b]!=col[c]:
            if col[b]<col[c]:
                if c-L<0:
                   break

                tmp=[]
                for d in range(c-L, c):
                    if [a, d] in slopes or col[c]-1!=col[d]:
                        break

                    tmp.append([a, d])

                else:
                    slopes+=tmp

                    continue

                break

            elif col[b]>col[c]:
                if b+L>=N:
                    break

                tmp=[]
                for d in range(b+1, b+L+1):
                    if [a, d] in slopes or col[b]-1!=col[d]:
                        break

                    tmp.append([a, d])

                else:
                    slopes+=tmp

                    continue

                break

    else:
        print(col)

        answer+=1

print(answer)