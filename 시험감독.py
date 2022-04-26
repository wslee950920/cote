N=int(input())
A=list(map(int, input().split(' ')))
B, C=map(int, input().split(' '))
print(N, A, B, C)

answer=0
for a in A:
    start=1
    end=1000001

    rst=0
    while start<=end:
        mid=(start+end)//2

        n=B+C*(mid-1)
        if a<=n:
            end=mid-1

            rst=mid

        else:
            start=mid+1
    answer+=rst
print(answer)