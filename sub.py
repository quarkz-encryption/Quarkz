def subtract(n1, n2):
    n1 = n1
    while n2 != 0:
        borrow = ((~n1) & n2)
        n1 = n1 ^ n2
        n2 = borrow << 1
    return n1


print (subtract(7, 2))
