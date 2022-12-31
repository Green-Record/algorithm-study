n = int(input())
array = [list(input()) for _ in range(n)]

rs=[]
def sol(a,b,n):
    std = array[a][b]
    for i in range(a,a+n):
        for j in range(b,b+n):
            if array[i][j]!=std:
                rs.append('(')
                sol(a,b,n//2)
                sol(a,b+n//2,n//2)
                sol(a+n//2,b,n//2)
                sol(a+n//2,b+n//2,n//2)
                rs.append(')')
                return
    rs.append(std)
sol(0,0,n)
print(''.join(rs))