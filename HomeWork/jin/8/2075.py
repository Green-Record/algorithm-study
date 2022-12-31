n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

rs = sorted(sum(li, []), reverse=True)
<<<<<<< HEAD
print(rs[n-1])
=======
print(rs[n-1])
>>>>>>> 7a3cdc4a5b13dffd40d8c4a78f9db20b54791455
