class BigThree:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def callBig(self):
        d=self.a if self.a>self.b else  self.b if self.a >self.c else self.c
        return d

a=int(input("Enter a 1st No."))
b=int(input("Enter a 2nd No."))
c=int(input("Enter a 3rd No."))

big=BigThree(a,b,c)
print(big.callBig())
