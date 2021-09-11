if __name__=='__main__':
    a=input("Enter the character:")
    while a != '$':
        if ord(a) >=65 and ord(a)<=90:
            print("The given character is upper",a)
        elif ord(a)>=96 and ord(a)<=122:
            print("The given character is lower",a)
        elif ord(a)>=46 and ord(a)<=57:
            print("The given character is digit", a)
        else:
            print("The given character is special",a)
        a=input("Enter the character:")

