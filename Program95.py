if __name__=='__main__':
    L=[]
    i=0
    L.append(input("Enter the character"))
    while L[i] !='$':
        i+=1
        L.append(input("Enter the character"))
    L.append('.')
    j=0
    linecount=0
    wordcount=0
    while L[j] !='.':
        if L[j]=="\\n":
            linecount+=1
            print("linecount",linecount)
        if L[j]==" ":
            wordcount+=1
            print("wordcount",wordcount)
        j+=1
    print(linecount)
    print(wordcount)


