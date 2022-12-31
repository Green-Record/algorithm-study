n, m = map(int,input().split())
li = list(map(int,input().split()))

start, end = 0, 1
cnt = 0
while start<=end and end<=n:
    rs = sum(li[start:end])
    if rs==m:
        cnt+=1
        end+=1
        start+=1
    elif rs<m:
        end+=1
    elif rs>m:
        start+=1
print(cnt)
    