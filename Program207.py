if __name__=='__main__':
    def big(a,b):
        if a > b:
            return a
        else:
            return b

    a=int(input("Enter the 1st No."))
    b=int(input("Enter the 2nd No."))
    print("The biggest of two No. is",big(a,b))