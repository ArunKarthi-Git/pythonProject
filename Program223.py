if __name__=='__main__':

    def read(L):
        L.append(input("Enter the character"))
        i=0
        while L[i]!='$':
            i+=1
            L.append(input("Enter the character"))
        L[i]='.'
    def readPattern(M):
        M.append(input("Enter the character To replace"))
        i = 0
        while M[i] != '$':
            i += 1
            M.append(input("Enter the character To replace"))
        M[i]='.'

    def replacePattern(M):
        M.append(input("Enter the character To new word"))
        i = 0
        while M[i] != '$':
            i += 1
            M.append(input("Enter the character To new word"))
        M[i]='.'


    def replace(L,L1,L2):
        L3 = []
        k = 0
        # for k in range(k,len(L)-1):
        while k < len(L):
            l = k
            m = 0
            print("k=", k)
            for m1 in range(m, len(L1)):
                print(L1[m1], "==", L[l])
                if L1[m1] == L[l] and L1[m] != '.':
                    l += 1
                    continue
                if L1[m1] == '.':
                    o = 0
                    for o1 in range(o, len(L2) - 1):
                        L3.append(L2[o1])
                        continue
                    k = l
                    break
                if L1[m1] != L[l] and L1[m1] != '.':
                    L3.append(L[l])
                    k += 1
                    break
        return L3

    L=[]
    M=[]
    N=[]
    read(L)
    readPattern(M)
    replacePattern(N)
    c=replace(L,M,N)
    print("The replaced Pattern is",c)