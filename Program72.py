if __name__=='__main__':

    matrix = []
    print("Enter the entries rowwise:")
    i=0
    while i<3:
        i+=1
        a=[]
        j=0
        while j<3:
            j+=1
            a.append(int(input()))
        #print(a)
        matrix.append(a)
    matrix1 = []
    print("Enter the entries rowwise:")
    i = 0
    while i < 3:
        i += 1
        b = []
        j = 0
        while j < 3:
            j += 1
            b.append(int(input()))
        # print(a)
        matrix1.append(b)
    #print(matrix)
    i=0
    while i<3:
        j=0
        while j <3:
            #print(i,j)
            #print(matrix[i][j])
            print(matrix[i][j], end=" ")
            j+=1
        i+=1
        print()
    print()
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            # print(i,j)
            # print(matrix[i][j])
            print(matrix1[i][j], end=" ")
            j += 1
        i += 1
        print()
    print()

    i = 0
    while i < 3:
        j = 0
        while j < 3:
            # print(i,j)
            # print(matrix[i][j])
            print(matrix[i][j]+matrix1[i][j], end=" ")
            j += 1
        i += 1
        print()