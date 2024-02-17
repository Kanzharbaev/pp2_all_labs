import math
degree=int(input("Input degree: "))
radian=math.radians(degree)
print(f"Output radian: {radian}")  #ex1

Heigh=int(input("Heigh: "))
fv=int(input("Base, first value: "))
sv=int(input("Base, second value: "))
area=(fv+sv)/2*Heigh
print(f"Expected Output: {area}") ##ex 2

n=int(input("Input number of sides: "))
l=int(input("Input the length of a side: "))
area1=(n*(l**2))/(4*math.tan(math.pi/n))
print(f"The area of the polygon is: {round(area1)}")  ##ex 3

leng=int(input("Length of base: "))
hei=int(input("Heigh of parallelogram: "))
area3=float(leng*hei)
print(f"Expected Output: {area3}")  ##ex 4