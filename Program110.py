if __name__=='__main__':
    L=[]
    L.append(int(input("Enter the No.")))
    j=0
    for i in L:
        if i == -100:
            continue
        if(L[j]>0):
            print("print the given no. is positive")
        elif(L[j]<0):
            print("print the given no. is negative")
        else:
            print("print the given no. is zero")
        j+=1
        L.append(int(input("Enter the No.")))

