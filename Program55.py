if __name__=='__main__':
    a=input("Enter the character:")
    while a !='$':
        if int(a) >=0 and int(a)<=9:
            print("Enter char is digit",int(a))
        elif a >='a' and a<='z':
            print("Enter char is lower",a)
        elif a >='A' and a<='Z':
            print("Enter char is upper",a)
        else:
            print("Enter char is special",a)
        a=input("Enter the character:")
