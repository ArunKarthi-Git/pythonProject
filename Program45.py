if __name__=='__main__':
    a=int(input("Enter a first value:"))
    b=int(input("Enter a second value:"))
    while a <= b:
        if a % 2 ==0:
            print("The  value {0} is even of {1}".format(a,b))
        else:
            print("The  value {0} is odd of {1}".format(a,b))
        a +=1