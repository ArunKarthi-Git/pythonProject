class sphere:
    def __init__(self,pi,radius):
        self.radius=radius
        self.pi=pi
    def calSphere(self):
        callSphere=4/3*self.pi*self.radius*self.radius;
        return callSphere

r=int(input("Enter the radius"))
pi=3.14
s=sphere(r,pi)
print(s.calSphere())