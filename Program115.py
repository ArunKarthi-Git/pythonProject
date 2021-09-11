if __name__=='__main__':
    L=[]
    L.append(input("Enter the character"))
    j=0
    for i in L:
        if i !='$':
            print(i)
        else:
            continue
        L.append(input("Enter the character"))
    print(L)