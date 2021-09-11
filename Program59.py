if __name__=='__main__':
    i=0
    a=big=0
    while i<10:
        a = int(input("Enter a value:"))
        if a>=big:
           big=a
        i+=1
    print("The biggest of 10 No. is",big)

