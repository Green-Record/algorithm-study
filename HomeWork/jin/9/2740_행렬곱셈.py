n1,m1 = map(int,input().split())
array1 = [list(map(int,input().split())) for _ in range(n1)]
n2,m2 = map(int,input().split())
array2 = [list(map(int,input().split())) for _ in range(n2)]

# print(array1,array2)
for i in range(n1):
    for j in range(m2):
        rs = 0
        for k in range(m1):
            rs+=array1[i][k]*array2[k][j]
        print(rs,end=' ')
    print()