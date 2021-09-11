if __name__=='__main__':

    matrix = []
    print("Enter the entries rowwise:")
    i=0
    while i<2:
        i+=1
        a=[]
        j=0
        while j<2:
            j+=1
            a.append(int(input()))
        #print(a)
        matrix.append(a)
    #print(matrix)
    i=0
    while i<2:
        j=0
        while j <2:
            #print(i,j)
            #print(matrix[i][j])
            print(matrix[j][i], end=" ")
            j+=1
        i+=1
        print()