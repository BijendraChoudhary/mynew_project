'''
rollno=[1,2,3,4,5]
def attendance():
 r=int (input("Enter roll no"))
 for r in (rollno):
    print("present")
 else:
    print("apsent")
    
attendance()
'''
'''
def add(n1,n2):
 sum=n1+n2
 print("sum of the two digit no is ",sum)

def sub(n1,n2):
 subs=n1-n2
 print("Substrac of the two digit no is",subs)

def mult(n1,n2):
 mult=n1*n2
 print("multiply of the two digit no is",mult)

def divide(n1,n2):
 div=n1/n2
 print("divide of the two digit no is",div)
n1=int(input("Enter first No"))
n2=int(input("Enter second No"))
opr=input("Enter the operation: +,-,*,/")
if opr=="+":
  add(n1,n2)
elif opr=="-":
   sub(n1,n2)
elif opr=="*":
   mult(n1,n2)
elif opr=="/":
   divide(n1,n2)
else:
   print("No operation for the no, sorry")
'''
'''
class myclass():
 def __init__(self,name1,name2):
     self.name1=name1
     self.name2=name2
     print("hello python",self.name1,"and",self.name2)
 def display(self):
  print("hello cdac",self.name1)
ob=myclass("peter","john")
ob.display()
'''
'''
class person:
  def __init__ (self,name1):
   self.name1=name1
   print("Good morning",name1)
  
 def display(self):
  print("Good bye",self.name1)
  
 def message(self):
   print("This is a class object")
    
ob1=person("John")
ob1.message()
ob1.display()
ob1.name1="Mohan"
ob2=person(ob1.name1)
ob2.display()
#ob.name="harry"
'''
'''
class sum:
# def __init__(self):
#self.n1=n1
#self.n2=n2
  def result(self):
   self.n1=n1
   self.n2=n2
   print(self.n1+self.n2)
n1=int(input("enter first no"))
n2=int(input("enter second no"))

ob=sum()
ob.result()
'''

'''
class div:
 def result(self):
     n=int(input("enter the no, divisible by 11")) 
     self.n=n
     if (self.n%11==0):
      print("divisible")
     else:
      print("not divisible")
   
ob=div()
ob.result()
'''
'''
class student:
    x="good morning"
    def name(self,age):
        self.age=age
        print("student age is :",self.age)
    def msg(self):
        print("Welcome to CDAC")

age=int(input("enter the age:"))
st=student()
st.name(age)
st.msg()
print(st.x)
'''
'''
class student:
    x="good morning"
    age=int(input("enter the age:"))
    def name(self,age):
        self.age=age
        print("student age is :",self.age)
    def msg(self):
        print("Welcome to CDAC")

class student2:
    def display():
        print(st.age)

st=student()
st.name(st.age)
st.msg()
print(st.x)
st2=student2
st2.display()
'''
'''
class employees:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def details(self):
        print("Employee name:",self.name)
        print("Employee salary:",self.salary)
        print("\n")

first=employees("Khush",10000)
second=employees("Raam",20000)
third=employees("Lav",10000)
fourth=employees("Sita",30000)
fifth=employees("Lucky",50000)

first.details()
second.details()
third.details()
fourth.details()
fifth.details()


m=90
n=7
print(m%n)

m=79
n=64
print(m<n)


class student:
    count=0
    def details (self,name,age):
        self.name=name
        self.age=age
        student.count+=1
    def display(self):
        print("student name"+self.name+"and the age is ",self.age)
    def total(self):
        print("Total student is ",student.count)

ob=student()
ob.details("John",25)
ob.display()
ob.details("hary", 56)
ob.display()
#ob.total()
ob2=student()
ob2.details("Ravi",39)
ob2.display()
ob2.total()


class student:
    count=0
    def details (self,name,age):
        self.name=name
        self.age=age
        student.count+=1
    def display(self):
        print("student name"+self.name+"and the age is ",self.age)
    def total(self):
        print("Total student is ",student.count)
name=input("enter student name :")
age=int(input("enter the age :"))
ob=student()
ob.details(name,age)
ob2=student()
ob2.details(name,age)
ob2.display()
ob2.total()

class parent:
    def display(self,x,y):
        self.x=x
        self.y=y
x=int(input("enter first no "))
y=int(input("enter second no :"))
class child(parent):
    def display2(self):
        sum=x+y
        print("sum of x and y is :",sum)

ob=child()
ob.display(x,y)
ob.display2()


class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname,self.lname)
class student(person):
    pass
x=student("Mike","Mohan")
x.printname()

class employee:
    'common base class for all employees'
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        employee.empCount+=1
        
    def displaycount(self):
        print("total employees: %d" %(self.empCount))
        
    def displayemployee(self):
        print("Name :",self.name)
        
ob=employee("RAM",5353)
ob.displaycount()
ob.displayemployee()


class one: #parent class
    def display1(self):
        print("this is one class")

class two:
     def display2(self):
         print("this is second class")

class three(one,two):
     def display3(self):
         print("this is third class")

ob=three()
ob.display1()
ob.display2()
ob.display3()
 '''

class one: #parent class
  x=int(input("enter one no"))
def display1(self):
        self.x=x
        print("this is one class")

class two:
    
 def display2(self):
    print("this is second class")
    y=int(input("enter second no"))
    self.y=y
class three(one,two):
        sum=self.x+self.y
def display3(self):
         print("sum of one and second no is :",sum)

ob=three()
ob.display1()
ob.display2()
ob.display3()















