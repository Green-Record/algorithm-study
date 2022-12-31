n = int(input())
array = [list(map(int,input().split())) for _ in range(n)]

cnt0,cnt1=0,0
def sol(a,b,n):
    global cnt0,cnt1
    std = array[a][b]
    for i in range(a,a+n):
        for j in range(b,b+n):
            if array[i][j]!=std:
                sol(a,b,n//2)
                sol(a,b+n//2,n//2)
                sol(a+n//2,b,n//2)
                sol(a+n//2,b+n//2,n//2)
                return
    if std==1:
        cnt1+=1
    elif std==0:
        cnt0+=1
sol(0,0,n)
print(cnt0)
print(cnt1)