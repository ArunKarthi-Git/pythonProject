if __name__=='__main__':
    def read(L):
        i=100
        L.append(input("Enter the character"))
        for j in range(i):
            if L[j] !='$':
                L.append(input("Enter the character"))
            else:
                break
        L.append('.')

    def display(L):
        w=l=c=0
        for i1 in range(len(L)):
            if L[i1] != '.':
                if L[i1] != ' ' and L[i1 + 1] == '':
                    w += 1
                if L[i1] == "\\n":
                    l += 1
                c = i1
        print("The word count is", w + 1)
        print("The line count is", l)
        print("The character count is", c)

    L=[]
    read(L)
    display(L)