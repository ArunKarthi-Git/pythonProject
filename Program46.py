if __name__=='__main__':
    a=int(input("Enter the begining year:"))
    b=int(input("Enter the end year:"))
    while a <= b:
        if a % 4 == 0:
            print("Printing year is {0} is leap year".format(a))
        else :
            print("printing year is {0} is not leap year".format(a))
        a +=1