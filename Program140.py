if __name__=="__main__":
    L=[]
    i=100
    w=c=l=0
    L.append(input(""))
    for i1 in range(i):
        if L[i1] !='$':
            L.append(input(""))
        else:
            break

    L[i1]='.'
    for i1 in range(len(L)):
        if L[i1] !='.':
            if L[i1] != ' ' and L[i1 + 1] == ' ':
                w += 1
            if L[i1] == "\\n":
                l += 1
            c = i1
    print("The word count is",w+1)
    print("The line count is", l)
    print("The character count is", c)
