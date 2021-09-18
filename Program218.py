if __name__=='__main__':

    def read(L):
        L.append(input("Enter the character"))
        i=0
        while L[i] !='$':
            i += 1
            L.append(input("Enter the character"))

    def copy(A,B):
        i=0
        while A[i]!='$':
            B.append(A[i])
            i+=1
    def display(B):
        i=0
        while i <len(B):
            print(B[i])
            i+=1
    def display(B):
        print(B)
    L=[]
    L=[]
    M=[]
    read(L)
    copy(L,M)
    display(M)
