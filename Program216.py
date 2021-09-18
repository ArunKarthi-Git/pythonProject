if __name__=='__main__':
    def Read(L):
        L.append(input("Enter the Character"))
        i=100
        for j in range(i):
            if L[j] !='$':
                L.append(input("Enter the Character"))
            else:
                break

    def Display(L):
        i=len(L)
        u=l=d=s=0
        for j in range(i):
            print(L[j])
            if L[j]=='':
                s+=1
            elif ord(L[j]) >= 65 and ord(L[j]) <= 90:
                u+=1
            elif ord(L[j]) >= 96 and ord(L[j]) <= 122:
                l+=1
            elif ord(L[j]) >= 46 and ord(L[j]) <= 57:
                d+=1
            else:
                s+=1
        print("count of upper",u)
        print("count of lower", l)
        print("count of digit", d)
        print("count of spl", s)


    L=[]
    Read(L)
    Display(L)


