if __name__=='__main__':

    def circle(r):
        return 3.14*r*r

    def sphere(r):
        return 4.0/3.0*3.14*r*r

    def cylinder(r,h):
        return 3.14*r*h

    a=int(input("Enter a no. for area"))
    print("The area of circle is:",circle(a))

    b=int(input("Enter a no.for sphere"))
    print("The area of sphere is:",sphere(b))

    c=int(input("Enter a radius for sphere"))
    d=int(input("Enter a height for sphere"))
    print("The area of cylinder is:",cylinder(c,d))
