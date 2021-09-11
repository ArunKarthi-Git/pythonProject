class area:
    def __init__(self,rad):
        self.rad=rad

    def calculateArea(self):
        area=3.14*self.rad*self.rad
        return area

rad1=int(input("Enter the rad"))
area1=area(rad1)
cal1=area1.calculateArea()
print("The calculated area is:",cal1)

