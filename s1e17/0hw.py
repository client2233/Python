i = 1
j = 9

while i < 9:
    j = 9
    while j > i:
        print (j, ' * ', i, ' = ', i*j, end="  ")
        j -= 1
    i += 1
    print()