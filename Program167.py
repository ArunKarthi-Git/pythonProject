class smallThree:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def callSmall(self):
        #d=self.a if self.a < self.b and self.a < self.c else self.c if self.b < self.c  else self.b
        small=0
        if self.a < self.b and self.a<self.c:
            small=self.a
        elif self.b < self.a and self.b < self.c:
            small=self.b
        else:
            small=self.c
        return small

a=int(input("Enter the 1st No."))
b=int(input("Enter the 2nd No."))
c=int(input("Enter the 3rd No."))

s=smallThree(a,b,c)
print("The Smallest of three No. is",s.callSmall())