if __name__=='__main__':
    L=[]
    L.append(input("Enter the Character"))
    for i in L:
        if i !='$':
            if ord(i)>=65 and ord(i)<=90:
                print("The given character is upper")
            elif ord(i)>=97 and ord(i)<=122:
                print("The given character is lower")
            elif ord(i)>=48 and ord(i)<=57:
                print("The given character is digit")
            else:
                print("The given character is spl")
        else:
            continue
        L.append(input("Enter the character"))
