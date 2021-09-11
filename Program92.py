if __name__=='__main__':
    s="A:=10;"
    i=0
    s1=""
    s2=""
    while i <len(s):
        if(s[i]==':'or s[i]==';'):
           s2=s[i]
        else:
            s1=s1+(s[i])
        i += 1
    print(s1)
