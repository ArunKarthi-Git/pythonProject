if __name__=='__main__':
    L=[]
    a=input("Enter a value")
    while a !='$':
        L.append(a)
        a = input("Enter a value")
    b=0
    while b<= len(L)-1:
        if L[b] == "Karthi":
            print(L[b],"is in poation",b)
        b+=1

