k, n = map(int,input().split())
li = [int(input()) for _ in range(k)]
start, end = 1, sum(li)//n

while start<=end:
    mid = (start+end)//2
    sumV = 0
    for i in li:
        sumV+=i//mid
    if sumV>=n:
        start=mid+1
    else:
        end = mid-1
print(end)