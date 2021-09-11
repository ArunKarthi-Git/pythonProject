if __name__=='__main__':
    a=int(input("Enter a value:"))
    sumPostive=sumNegative=zero=0
    while a != -100:
        if a > 0:
            sumPostive+=a
        elif a<0:
            sumNegative+=a
        else:
            zero+=a
        a=int(input("Enter a value:"))
    print("Sum of postive No. is:",sumPostive)
    print("Sum of negative No. is:",sumNegative)
    print("Sum of zero No. is:", zero)
