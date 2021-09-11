if __name__=='__main__':
    L=[]
    i=0
    while i <10:
        L.append(int(input("Enter a No.")))
        i+=1
    i=0
    big=bigp=0
    while i < 10:
        if L[i] > big:
            big=L[i]
            bigp=i
        i+=1
    i=smallp=0
    small=L[i]
    while i < 10:
        if L[i]< small:
            small=L[i]
            smallp=i
        i+=1
    temp=big
    L[bigp]=small
    L[smallp]=temp
    j=0
    while j < 10:
        print(L[j])
        j+=1
