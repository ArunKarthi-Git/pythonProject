if __name__=='__main__':
    L=[]
    upperCount=0
    lowerCount=0
    noCount=0
    splCount=0
    L.append(input("Enter the Character"))
    for i in L:
        if i !='$':
            if i>='A' and i<='Z':
                upperCount+=1
            elif i>='a' and i<='z':
                lowerCount+=1
            elif i>='0' and i<='9':
                noCount+=1
            else:
                splCount+=1
        else:
            continue
        L.append(input("Enter the Character"))
    print("Upper character count is:",upperCount)
    print("Lower character count is:", lowerCount)
    print("No character count is:", noCount)
    print("Spl character count is:", splCount)
