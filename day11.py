'''
class student:
    def __init__ (self,age,roll):
        self.age=age
        self.roll=roll
    def display(self):
        print(self.age,self.roll)

class s1(student):
    def __init__ (self,age,roll):
        student.__init__ (self,age,roll)
        print("welcome to class")
st=s1(3,4)
st.display()


class student:
    def __init__ (self,age,roll):
        self.age=age
        self.roll=roll
    def display(self):
        print(self.age,self.roll)

class s1(student):
    def __init__ (self,age,roll):
        student.__init__ (self,age,roll)
        print("welcome to class")
    def location(self,area):
        self.area=area
        print("location of student is",self.area)
        
st=s1(3,4)
st.display()
st.location("noida")


class student:
    def __init__ (self,age,roll):
        self.age=age
        self.roll=roll
    def display(self):
        print(self.age,self.roll)

class s1(student):
    def __init__ (self,age,roll):
        student.__init__ (self,age,roll)
        print("welcome to class")
    #def location(self,area):
        self.area="noida"
     #   self.area=area
        print("location of student is",self.area)
        
st=s1(3,4)
st.display()
#st.location("noida")


class student:
    def __init__ (self,age,roll):
        self.age=age
        self.roll=roll
    def display(self):
        print(self.age,self.roll)

class s1(student):
    def __init__ (self,age,roll):
        super().__init__ (age,roll)
        print("Age is :",self.age,"and roll no is :",self.roll)
        print("welcome to class")
    #def location(self,area):
        self.area="noida"
     #   self.area=area
        print("location of student is",self.area)
        
st=s1(3,4)
st.display()

class student:
    def __init__ (self,age,roll):
        self.age=age
        self.roll=roll
    def display(self):
        print(self.age,self.roll)

class s1(student):
    def __init__ (self,age,roll):
        super().__init__ (age,roll)
        print("Age is :",self.age,"and roll no is :",self.roll)
        print("welcome to class")
        self.area="noida"
        print("location of student is",self.area)

age=int(input("enter age :"))
roll=input("enter roll no :")        

st=s1(age,roll)
st.display()


class first:
    def display1(self):
        self.x=int(input("enter first no :"))
#        print("value of x is :",self.x)

class second:
    def display2(self):
        self.y=int(input("enter second no :"))
#       print("value of y is :",self.y)

class third(first,second):
    def display3(self):
        super().display1()
        super().display2()
        self.z=self.x+self.y
        print("sum of two nos is :",self.z)

ob=third()
#ob.display1()
#ob.display2()
ob.display3()


class parent1:
    def display1(self):
     print("welcome to CDAC")

class parent2:
    def display2(self):
     print("CDAC is in Sec-62")

class child(parent1,parent2):
    def display3(self):
     super().display1()
     super().display2()

ob=child()
ob.display3()


class fruit:
    def display1(self,fru):
        self.fru=fru
        print("fruit name is :",self.fru)
class mango:
    def display2(self):
        super().display1()
        
fru=input("enter fruit name :")

ob=fruit()
ob.display1

class parent1:
    def func1(self):
        print("This is the first parent class")
        
class parent2(parent1):
    def func3(self):
        print("This is the 2nd parent class")

class child(parent2):
    def func2(self):
        print("This is the child class")

#ob=child()
#ob.func1()
ob1=parent2()
ob1.func1()
ob1.func3()


class parent1:
    def func1(self):
        print("This is the first parent class")
        
class parent2(parent1):
    def func3(self):
        print("This is the 2nd parent class")

class parent3:
    def func4(self):
        print("This is the 3rd parent class")

class child(parent1,parent3):
    def func2(self):
        print("This is the Parent class")

#ob=child()
#ob.func1()
#ob.func4()
ob1=parent2()
ob1.func1()
'''
