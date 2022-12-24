n, m = map(int, input().split())
li = list(map(int, input().split()))

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
