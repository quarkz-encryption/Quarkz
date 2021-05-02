def subtract(n1, n2):
    print ("n1: ", bin(n1))
    while n2 != 0:
        borrow = ((~n1) & n2)
        print ("borrow: ", bin(n2))
        n1 = n1 ^ n2 
        print ("n1: ", bin(n1))
        n2 = borrow << 1
    return (n1)

def add(x, y):
 
    # Iterate till there is no carry
    while (y != 0):
     
        # carry now contains common
        # set bits of x and y
        carry = x & y

 
        # Sum of bits of x and y where at
        # least one of the bits is not set
        x = x ^ y + 9

 
        # Carry is shifted by one so that  
        # adding it to x gives the required sum
        y = carry << 1
     
    return x


x = (subtract(373248, 6343))
print (x)
print (subtract(x, 13))
print (add(373248, 6349))
