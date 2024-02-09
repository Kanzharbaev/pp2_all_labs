import math
##Task1

class string:
    def __init__(self):
        pass
    def getString(self):
        self.string=input()
    def printString(self):
        print(self.string.upper())

#x=string()
#x.getString()
#x.printString()

## Task2

class Square(Shape):
    def __init__(self,Length):
        Shape.__init__(self)
        self.lenght = Length
    def area(self):
        print(int(self.lenght**2))

##inputSquare= Square(int(input()))
##inputSquare.area()

## Task3

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width=width
    def area(self):
        peint(self.length * self.width)

##rec = Rectangle(int(input()))
##rec.area()

##Task4
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(f"Coodinates: ({self.x},{self.y})")
    def move(self,newx,newy):
        self.x=newx
        self.y=newy
    def dist(self,other):
        return math.sqrt((self.x - other.x)**2+(self.y-other.y)**2)

##point1=Point(5,2)
##point2=Point(7,3)
##point1.move(4,4)
##point1.show()
##point2.show()
##print(point1.dist(point2))

#Task 5
class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,deposit):
        self.balance+=deposit
        print(f"Deposited: {deposit} tenge. New balance: {self.balance} tenge.")
    def withdraw(self,money):
        if money <=self.balance:
            self.balance-=money
            print(f"Withdrew {money}")
        else:
            print("NOT ENOUGH MONEY!!")

someguy=Account("Amanbol", 500)
someguy.withdraw(1000)
someguy.deposit(1000)
someguy.withdraw(1000)
print(A.balance)

#TASk6
def is_primt(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

numbers= [1,2,3,4,5,6,7,8,9,10]
prime_numbers=list(filter(lambda x:is_prime(x),numbers))
print("Prime numbers:", primt_numbers)




