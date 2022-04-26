from functools import reduce

N=int(input())
A=list(map(int, input().split(' ')))
M=list(map(int, input().split(' ')))

mx=-10**9
mn=10**9

def dfs(now, mlst):
    global mx, mn

    if len(now)==N-1:
        #print(now)

        rst=A[0]
        for i in range(N-1):
            #print(rst, now[i], A[i+1])

            if now[i]==0:
                rst+=A[i+1]

            elif now[i]==1:
                rst-=A[i+1]

            elif now[i]==2:
                rst*=A[i+1]

            elif now[i]==3:
                if rst<0:
                    rst=-(abs(rst)//A[i+1])

                else:
                    rst//=A[i+1]
            #print(rst)

        mx=max(mx, rst)
        mn=min(mn, rst)

        return

    for j, m in enumerate(mlst):
        if m==0:
            continue

        mlst[j]-=1
        dfs(now+[j], mlst)
        mlst[j]+=1
dfs([], M)

print(mx)
print(mn)