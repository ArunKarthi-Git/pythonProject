if __name__=='__main__':
    s="A=10\n"
    i=0
    s1=""
    while i <len(s):
        if(s[i]=='='):
            s1=s1+':'
        if (s[i] == '\n'):
            s1 = s1 + ';'
        s1=s1+s[i]
        i+=1
    print(s1)