if __name__=='__main__':
    L=[]
    i=100
    u=l=d=s=0
    L.append(input("Enter the Character"))
    for i1 in range(i):
        if L[i1] !='$':
            L.append(input("Enter the Character"))
        else:
            break
    L[i1]='.'

    for i1 in range(len(L)):
            if ord(L[i1]) >=65 and ord(L[i1])<=90:
                u+=1
            elif ord(L[i1]) >=97 and ord(L[i1])<=122:
                l+=1
            elif ord(L[i1])>=48 and ord(L[i1])<=57:
                d+=1
            else:
                s+=1
    print("The count of upper char:",u)
    print("The count of lower char:", l)
    print("The count of digit char:", d)
    print("The count of spl char:", s)