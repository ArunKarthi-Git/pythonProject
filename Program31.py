if __name__=='__main__':
    a=ord(input("Enter the character"))
    if a>=97 and a<=122:
        print("Given character is lower")
    elif a>=65 and a<=90:
        print("Given Character is upper")
    elif a>=48 and a <=57:
        print("Given Character is interger")
    else:
        print("Given Character special")