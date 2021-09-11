if __name__=='__main__':
    i=0
    L=[]
    while i < 10:
       a=int(input("Enter a No."))
       L.append(a)
       i+=1
    j=0
    big=0
    postion=0
    while j < 10:
        if L[j] > big:
            big=L[j]
            postion=j+1
        j+=1
    print("The Postion of big is:",postion)

