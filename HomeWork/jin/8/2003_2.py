<<<<<<< HEAD
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
=======
n, m = map(int,input().split())
li = list(map(int,input().split()))

dp =[0]
sum = 0
for i in li:
    sum+=i
    dp.append(sum)

start, end = 0, 1
cnt=0
while start<=end and end<=n:
    rs = dp[end]-dp[start]
    if rs==m:
        cnt+=1
        start+=1
        end+=1
    elif rs>m:
        start+=1
    else:
        end+=1
print(cnt)
>>>>>>> 7a3cdc4a5b13dffd40d8c4a78f9db20b54791455
