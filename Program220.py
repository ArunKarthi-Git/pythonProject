from  Program219 import read
if __name__=='__main__':
    def read(L):
        L.append(input("Enter the Character"))
        i=0
        while(L[i]!='$'):
            i+=1
            L.append(input("Enter the Character"))

    def copy(A,B,p,q):
        print(len(A),p,q)
        i=0
        while p <= len(A) and i<q:
            B.append(A[p])
            p+=1
            i+=1



    L=[]
    R=[]
    read(L)
    n=int(input("Enter a No. character to copy"))
    m=int(input("Enter a No. from which character to copy"))
    copy(L,R,n,m)
    print(R)