n, m = map(int, input().split())
li = list(int(input()) for _ in range(n))
start, end = min(li), sum(li)

while start <= end:
    mid = (start + end) // 2
    charge = mid	
    cnt = 1	
    for i in range(n):		
        if charge < li[i]:	
            charge = mid
            cnt += 1
        charge -= li[i]	

    if cnt > m or mid < max(li):	
        start = mid + 1
    else:			
        end = mid - 1
        k = mid

print(k)