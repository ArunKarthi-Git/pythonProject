if __name__=='__main__':
    a=2000
    while a <= 2030:
        if a % 4 == 0:
            print("The year is leap:",a)
        else:
            print("The year is not leap:",a)
        a +=1