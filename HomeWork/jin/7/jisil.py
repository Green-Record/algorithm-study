"""
inp =
4
1 2 3 0
1 7 3 7
1 7 7 7
0 2 2 0

outp=
2
"""

n = int(input())
li = [list(map(int,input().split())) for _ in range(n)]
white = li = [[0]*n for _ in range(n)]

dic_start = dict()
dic_end = dict()

for i in range(n):
    for j in range(n):
        dic_start[li[i][j]]=dic_start.get(li[i][j],[i,j])
        dic_end[li[i][j]]=[i,j]
           
rs=1                    
for i in dic_start:
    flag=0
    for j in range(dic_start[i][0],dic_end[i][0]):
        for k in range(dic_start[i][1],dic_end[i][1]):
            if not white[j][k]:
                white[j][k]+=1
            else:
                white[j][k]+=1
                flag=1
    if not flag:
        rs+=1
print(rs)