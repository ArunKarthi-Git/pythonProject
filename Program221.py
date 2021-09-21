if __name__=='__main__':

    def read(L):
        L.append(input("Enter the character"))
        i=0
        while L[i]!='$':
            i+=1
            L.append(input("Enter the character"))
        L[i]='.'
    def readPattern(M):
        M.append(input("Enter the character To Search"))
        i = 0
        while M[i] != '$':
            i += 1
            M.append(input("Enter the character To Search"))
        M[i]='.'

    def count(L,L1):
        k = 0
        count = 0
        while L[k] != '.':
            M = 0
            N = k
            while L1[M] == L[N] and L1[M] != '.':
                M += 1
                N += 1
                if L1[M] == '.':
                    count += 1
            k += 1
        #print("pattern Exit", count, " times")
        return count

    L=[]
    M=[]
    read(L)
    readPattern(M)
    c=count(L,M)
    print(c)