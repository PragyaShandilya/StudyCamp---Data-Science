#Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

class calculator:
    def __init__(self,a,b,ch):
        self.a = a
        self.b = b
        self.ch = ch

    def add(self):
        print (self.a + self.b)
    def sub(self):
        print(self.a - self.b)
    def mul(self):
        print (self.a * self.b)
    def div(self):
        print( self.a / self.b )

a = int(input("Enter a: "))
b = int(input("Enter b: "))
ch = int(input("1.Add\n2.Subtract\n3.Multiply\n4.Divide\nEnter choice: "))
obj1 = calculator(a,b,ch)
if ch==1:
    obj1.add()
elif ch==2:
    obj1.sub()
elif ch==3:
    obj1.mul()
elif ch==4:
    obj1.div()
else:
    print("Invalid Statement")


