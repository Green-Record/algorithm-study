n = int(input())

rs=[0,1,2]
for i in range(3,n+1):
    rs.append(rs[i-1]+rs[i-2])
print(rs[n])