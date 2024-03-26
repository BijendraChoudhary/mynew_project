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
