n, m = map(int, input().split())
daily = list(int(input()) for _ in range(n))
start, end = 1, max(daily)

while start <= end:
    mid = (start + end) // 2
    charge = mid
    num = 1
    for i in range(n):
        if charge < daily[i]:
            charge = mid
            num += 1
        charge -= daily[i]
    if num > m or mid < max(daily):
        start = mid + 1
    else:
        end = mid - 1

print(k)

print(mid)
