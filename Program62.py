'''Read and mean 10 No. using array'''
if __name__=='__main__':
    L=[]
    i=0
    while i<10:
        L.append(int(input("Enter the No.")))
        i+=1
    j=0
    sum1=0
    mean=0
    while j<10:
        sum1+=L[j]
        j+=1
    mean=sum1/j
    print("Mean of 10 No. is",mean)