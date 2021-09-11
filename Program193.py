import sys

# python Program193.py /home/karthi/Document/file11.txt

if __name__=='__main__':
    argc=len(sys.argv)
    if argc !=2:
        print("Argument is not Valid")
        sys.exit(1)
    if sys.argv[1] is None:
        print("File not found")
        sys.exit(1)

    #with open(sys.argv[1],"r") as f:
    fp=open(sys.argv[1],"r")
    L=[]
    L.append(input("Enter the word"))
    i=0
    while L[i]!='.':
        i+=1
        L.append(input("Enter the word"))

    L[i]='.'
    c=0
    for line in fp:
        j=0
        for letter in line:
            for i in letter:
                print(L[j]," ",i)
                if L[j] == i  and L[j]!='.':
                    j+=1
            if L[j]=='.':
                c+=1
                j=0
    fp.close()
    print("Thw word is fount",c," time")

