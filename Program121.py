if __name__=='__main__':
    L=[]
    i=10
    big=0
    for j in range(i):
        L.append(int(input("Enter the No.")))
        '''if L > big:
            big=L'''
        big = L[j] if L[j] > big else big
    print("The biggest No. is:",big)
