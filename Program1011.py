if __name__=='__main__':
    T=()
    a=input("Enter a value")
    i=0
    List =[]
    while a !='$':
        List.append(a)
        a = input("Enter a value")
    print(tuple(List))
    print(len(tuple(List)))
    t=tuple(List)
    b=0
    while b<= len(tuple(List))-1:
        print(t[b])
        b+=1

