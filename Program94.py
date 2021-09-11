if __name__=='__main__':
    s="Hello \n How r u \n iam fine \n"
    #s=input("Enter the text")
    print(s)
    i=0
    l=0
    t=0
    while i<len(s):
        if s[i] == '\n':
            l+=1
        if s[i] == ' ':
            t += 1
        i+=1
    print("The no. of line is",l)
    print("The no. of text is", t)