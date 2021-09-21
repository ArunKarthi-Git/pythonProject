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

    def delete(L,L1):
        L2 = []
        k1 = 0
        # for k1 in range(k,len(L)):
        while k1 <= len(L) - 1:
            n = k1
            m = 0
            for m1 in range(m, len(L1)):
                print(L1[m1], "=", L[n])
                if L1[m1] == L[n] and L1[m1] != '.':
                    n += 1
                    continue
                if L1[m1] == '.':
                    k1 = n
                    # L2.append(L[k1])
                    break
                if L1[m1] != L[n] and L1[m1] != '.':
                    L2.append(L[k1])
                    k1 += 1
                    break
        return L2

    L=[]
    M=[]
    read(L)
    readPattern(M)
    c=delete(L,M)
    print(c)