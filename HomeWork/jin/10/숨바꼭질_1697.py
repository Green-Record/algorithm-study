from collections import deque

s, d = map(int,input().split())
array = [0]*100001

def bfs(n):
    if n==d:
        return 0
    q = deque()
    q.append(n)
    while q:
        n = q.popleft()
        for i in [n-1,n+1,2*n]:
            if 0<=i<100001 and not array[i]:
                array[i]=array[n]+1
                if i==d:
                    return array[d]
                q.append(i)
                

print(bfs(s))