if __name__=='__main__':
    L=[]
    i=100
    L.append(input())
    for i1 in range(i):
        if L[i1] !='$':
            L.append(input())
        else:
            break
    L[i1]='.'

    L1=[]
    L1.append(input("Enter the word to count"))
    for i1 in range(i):
        if L1[i1] !='$':
            L1.append(input("Enter the word to count"))
        else:
            break

    L1[i1]='.'
    k=0
    count=0
    for i1 in range(len(L)):
        j=0
        for j1 in range(j,len(L1)):
            k = i1
            print(L1[j1], "==", L[k])
            if L1[j1]==L[k] or L1[j1]=='.':
                i1+=1
                print(L1[j1])
                if L1[j1]=='.':
                    count+=1
            else:
                break
        continue

    print("The pattern count is:",count)