from collections import deque

n = int(input())

array=[list(map(int,input())) for _ in range(n)]

dx=[0,-1,1,0]
dy=[1,0,0,-1]

def dfs(x,y):
    global cnt
    array[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and array[nx][ny]:
            dfs(nx,ny)
            cnt+=1
            
def bfs(x,y):
    cnt=1
    q = deque()
    q.append([x,y])
    while(q):
        x,y = q.popleft()
        array[x][y]=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and array[nx][ny]:
                q.append([nx,ny])
                array[nx][ny]=0
                cnt+=1
    return cnt

# rs=[]
# for i in range(n):
#     for j in range(n):
#         if array[i][j]:
#             cnt=1
#             dfs(i,j)
#             rs.append(cnt)
            
rs=[]
for i in range(n):
    for j in range(n):
        if array[i][j]:
            rs.append(bfs(i,j))
            
print(len(rs))
rs.sort()
for i in rs:
    print(i)   