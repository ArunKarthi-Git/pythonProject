'''Read and find the biggest of 10 No. using List'''
if __name__=='__main__':
    L=[]
    i=0
    while i<10:
        L.append(int(input("Enter the value:")))
        i+=1
    Big=0
    j=0
    while j< 10:
        if Big < L[j]:
            Big=L[j]
        j+=1
    print("The Biggest No. is:",Big)

    while (i < j):
        print(i)
        i += 1
    i += 1
    j += 1
