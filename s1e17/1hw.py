i = 2

while i<=10:
    n = 2
    while n<i:
        if not i%n:
            print(i, "=", n, "*", i//n)
            break
        n += 1
    else:
        print(n, "是一个素数")
    i += 1