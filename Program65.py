if __name__=='__main__':
    L=[]
    i=big=small=0
    while i < 10:
       a = int(input("Enter a No."))
       L.append(a)
       i+=1
    j=0
    big=0
    while j < 10:
       if L[j] > big:
        big=L[j]
        bigp=j+1
       j+=1
    small=big
    i=0
    smallp = 0
    while i < 10:
       if L[i] < small:
        small=L[i]
        smallp=i+1
       i+=1
    print("The position of biggest No. is",bigp)
    print("The position of smallest No. is", smallp)
