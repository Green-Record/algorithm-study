n = int(input())
array = [list(map(int,input().split())) for _ in range(n)]

cntm1,cnt0,cnt1=0,0,0
def sol(a,b,n):
    global cntm1,cnt0,cnt1
    std = array[a][b]
    for i in range(a,a+n):
        for j in range(b,b+n):
            if array[i][j]!=std:
                for x in range(3):
                    for y in range(3):
                        sol(a+x*n//3,b+y*n//3,n//3)
                return
    if std==1:
        cnt1+=1
    elif std==0:
        cnt0+=1
    elif std==-1:
        cntm1+=1
sol(0,0,n)
print(cntm1)
print(cnt0)
print(cnt1)