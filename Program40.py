if __name__=='__main__':
    a=input("Enter the character or value:")
    if a=='a' or a=='b' or a=='c' or a=='d' or a=='e' or a=='f':
        print("enterd is char",a)
    elif a=='+' or a=='-' or a=='*' or a=='/':
        print("Enter is operator",a)
    elif int(a)>=0 and int(a) <=9:
        print("enter is no.",int(a))
    else:
        print("Enterd is ",a)