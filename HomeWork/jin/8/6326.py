n, m = map(int, input().split())
li = list(int(input()) for _ in range(n))
start,end = min(li), sum(li)

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    curV = mid
    for i in li:
        if curV < i:
            cnt+=1
            curV=mid
        curV-=i
    if cnt>m or mid<max(li):
        start = mid+1
    else:
        end = mid-1
        k = mid
print(k)