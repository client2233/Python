i = 1
j = 1

while i<=9:
    j = 1
    while j<=i:
        print (i, 'x', j, '=', i*j, end="  ")
        j += 1
    print ('\n')
    i += 1