if __name__=='__main__':
    L=[]
    i=0
    L.append(input("Enter the character"))
    while L[i] != '$':
        i+=1
        L.append(input("Enter the character"))
    L[i]='.'
    i=u=l=d=s=0
    while L[i]!='.':
        if ord(L[i])>=65 and ord(L[i])<= 90:
            u+=1
        elif ord(L[i])>=97 and ord(L[i])<= 122:
            l+=1
        elif ord(L[i])>=48 and ord(L[i])<=57:
            d+=1
        else:
            s+=1
        i+=1
    print("No. of upper character is:",u)
    print("No. of lower character is:", l)
    print("No. of digit character is:", d)
    print("No. of special character is:", s)
