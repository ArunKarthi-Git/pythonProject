if __name__=='__main__':
    L=[]
    i=0
    while i < 10:
        L.append(int(input("Enter the No.")))
        i+=1
    i=0
    big=0
    while i <10:
        if L[i] > big:
            big=L[i]
        i+=1

    i=0
    sbig=0
    while i<10:
        if L[i] > sbig and L[i] < big:
            sbig=L[i]
        i+=1

print("The Second Biggest No. is:",sbig)