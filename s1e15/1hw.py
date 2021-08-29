n = int(input("请输入一个正整数："))

while n > 0:
    if not n%2:
        print (n, "/2 = ", int(n//2))
        n = n//2
    else:
        print(n, "*3 +1 = ", n*3 + 1)
        n = n*3 + 1
    if n == 1:
        break

