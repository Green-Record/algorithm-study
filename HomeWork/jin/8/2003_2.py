cnt = 0
while start <= end and end <= n:
    rs = dp[end]-dp[start]
    if rs == m:
        cnt += 1
        start += 1
        end += 1
    elif rs > m:
        start += 1
    else:
        end += 1
print(cnt)
