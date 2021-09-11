if __name__=='__main__':
    a=int(input("Enter a value:"))
    while a !=0:
        if a > 0:
            print("Given No. is Positive")
        elif a < 0:
            print("Given No. is Negative")
        else :
            print("Given No. is Zero")
        a=int(input("Enter a value:"))
    print("Given No. is Zero")