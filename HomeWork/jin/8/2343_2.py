<<<<<<< HEAD
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
video = list(map(int, input().split()))

start = 1
end = sum(video)

while(start <= end):
    mid = (start+end)//2
    cnt = 1
    tmp = 0
    for i in range(n):
        if(tmp+video[i] <= mid):
            # 만약 현재 블루레이에 비디오를 더 넣을 수 있다면
            tmp += video[i]
        else:
            cnt += 1
            tmp = video[i]
        if(cnt > m):
            break
    if(cnt > m):
        start = mid+1
    else:
        end = mid-1

print(mid)
=======
n, m = map(int, input().split())
li = list(map(int, input().split()))

start = max(li)
end = res = sum(li)
while start <= end :
    mid = (start+end)//2
    cnt = 1
    sumV = 0
    for i in range(n):
        if sumV+li[i] <= mid:
            sumV += li[i]
        else:
            cnt += 1
            sumV = li[i]
        if cnt > m:
            break
    if cnt > m : # 조건을 만족하는 mid의 최솟값을 찾기 위해
        start = mid+1
    else:
        end = mid-1
        res=min(res,mid)
print(res)
>>>>>>> 7a3cdc4a5b13dffd40d8c4a78f9db20b54791455
