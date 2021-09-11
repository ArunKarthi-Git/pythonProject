if __name__=='__main__':
    L=[]
    L.append(input("Enter the Character"))
    for i in L:
        if i !='$':
            if i>='A' and i<='Z':
                print("The given character is upper")
            elif i>='a' and i<='z':
                print("The given character is lower")
            elif i>='0' and i<='9':
                print("The given character is digit")
            else:
                print("The given character is spl")
        else:
            continue
        L.append(input("Enter the character"))
