'''Read and display the ten No. Using Set'''
if __name__=='__main__':
    L=[]
    i=0
    while i<10:
      L.append(int(input("Enter a value")))
      i+=1
    j=0
    sum=0
    while j<10:
        sum+=L[j]
        j+=1
    print("Sum of 10 No. in array is:",sum)