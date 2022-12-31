n, m = map(int, input().split())
li = list(map(int, input().split()))

<<<<<<< HEAD
start, end = 1, sum(li)
while start <= end:
    mid = (start+end)//2
    cnt = sumV = 0
    rs = []
    for i in li:
        sumV += i
        if sumV >= mid:
            cnt += 1
            rs.append(sumV)
            sumV = 0
    if cnt >= m:
        start = mid+1
    else:
        end = mid - 1
print(max(rs))
=======
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
            print(sumV+li[i],mid,cnt,m)
            sumV = li[i]
        if cnt > m:
            break
    if cnt > m : # 조건을 만족하는 mid의 최솟값을 찾기 위해
        start = mid+1
    else:
        end = mid-1
        if cnt==m:
            res=min(res,mid)
print(res)
#9 4
#9 9 9 9 9 9 9 9 9
>>>>>>> 7a3cdc4a5b13dffd40d8c4a78f9db20b54791455
