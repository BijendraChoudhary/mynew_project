'''
def product(a,b):
    p=a*b
    print(p)

def product(a):
    p=a*a
    print(p)

def product(a,b,c):
    p=a*b*c
    print(p)

product(4,5,5)


class parent:
    def sum(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        self.x=self.a+self.b+self.c
        print("sum of 3 digit no is :",self.x)

class child:
    def sum(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        print(self.a*self.b*self.c)

c=child()
p=parent()
c.sum(2,3,4)
p.sum(2,3,4)


class parent:
    #constructor
    def __init__ (self):
        self.value="inside Parent"

    #parent's show method
    def show(self):
            print(self.value)
    #defining child class

class child(parent):
    def __init__ (self):
            self.value="inside child"
    #child's show method
    def show(self):
                print(self.value)

#obj1=parent()
obj2=child()
#obj1.show()
obj2.show()


class CDAC1:
    def __init__ (self,course,location):
        self.course=course
        self.location=location
    def display(self):
        print("This is CDAC1 method")

class CDAC2(CDAC1):
    pass

class CDAC3(CDAC1):
    def display(self):
        print("This is CDAC3 method")

class CDAC4(CDAC1):
    def display(self):
        print("This is CDAC4 method")

ob1=CDAC2("Python", "Noida")
ob2=CDAC3("Webrech","Delhi")
ob3=CDAC4("database","Pune")
ob1.display()
ob2.display()
ob3.display()
print(ob2.course,ob2.location)


class CDAC1:
    def __init__ (self,course,location):
        self.course=course
        self.location=location
    def display(self):
        print("This is CDAC1 method")

class CDAC2:
    def __init__ (self,course,location):
        self.course=course
        self.location=location
    def display(self):
        print("This is CDAC2 method")

class CDAC3:
    def __init__ (self,course,location):
        self.course=course
        self.location=location
    def display(self):
        print("This is CDAC3 method")

ob1=CDAC1("Python", "Noida")
ob2=CDAC2("Webrech","Delhi")
ob3=CDAC3("database","Pune")
for x in (ob1,ob2,ob3):
 x.display()
print(ob1.course,ob2.course,ob3.course)
print(ob1.location)


class student:
    def __init__ (self,x=0,y=0):
        self.x=x
        self.y=y

    def __str__ (self):
        return( "{0},{1}".format(self.x,self.y))

p1=student(2,4)
p2=student(-1,2)
print(p1)
print(p2)
print(p1.x+p2.x)
print(p1.y+p2.y)


class student:
    def __init__ (self,x=0,y=0):
        self.x=x
        self.y=y

    def __repr__ (self):
        return( "{0},{1}".format(self.x,self.y))
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return student(x,y)
    
p1=student(2,4)
p2=student(-1,2)
print(p1+p2)

class student:
    def __init__ (self,n1,n2):
        self.n1=n1
        self.n2=n2

    def  display(self):
        sum=self.n1+self.n2
        print("sum of n1 and n2 is :",sum)

n1=int(input("enter first no :"))
n2=int(input("enter second no:"))

ob=student(n1,n2)
ob.display()


class student:
    def __init__ (self,name,age):
        self.name=name
        self.age=age

    def __str__ (self):
        return("name is {0} and the age is {1}".format(self.name,self.age))

  

st=student("john",34)
print(st)
'''

class student:
    def __init__ (self,age):
        self.age=age

    def __add__(self,other):
        return student(self.age+other.age)

st1=student(34)
st2=student(34)
st3=st1+st2
print(st3.age)







    


    


        




