'''
class computer:
    def __init__(self):
        self.__price=2000 # private variable
        print("price is :",self.__price)

    def sell(self):
        print("selling price :",self.__price)

class laptop(computer):
    def lap(self):
        print(self.__price)

ob=laptop()
#ob.lap()
ob.sell()


class computer:
    def __init__(self):
        self._price=2000 # private variable
        print("price is :",self._price)

    def sell(self,value):
        self._price=value
        print("selling price :",self._price)

    def price(self,value):
        self.price=value
        print("change in price",self.price)

class laptop(computer):
    def lap(self):
        print(self._price)

#ob=laptop()
#ob.lap()
#ob.sell()
#ob.price(9000)
ob1=computer()
ob1.sell(5000)
ob1.price(10000)


from abc import ABC, abstractmethod
class XYZ(ABC): #base class inherits from ABC class
    @abstractmethod

    def func1(self):#abstract method named func1()
        print("this is the abstract class")

class anotherClass(XYZ):
    def func1(self):
        super().func1()
        print("this is class")

    def func2(self):
        super().func1()
        print("this is another class")
ob=anotherClass()
ob.func2()


class student:
    def __init__ (self,no1,no2):
        self._no1=90
        self._no2=95
        print("Nos is :",self._no1,self._no2)

    def total(self):
        print("sum of two no is ",self._no1+self._no2)

    def display(self):
        super().total()
        
class child(student):
    def stu(self):
        print("total ",self._no1+self._no2)

no1=int(input("enter first no:"))
no2=int(input("enter second no:"))

ob=child()
ob.stu()


from abc import ABC, abstractmethod
class Abstract(ABC):
    @abstractmethod
    def func1(self):
        print("this is the first abstract method")
    @abstractmethod
    def func2(self):
         print("this is the second abstract method")

class anotherClass(Abstract):
    def func1(self):
        super().func1()
        print("this is first derived method")

    def func2(self):
        print("this is second derived method")
        super().func2()

ob=anotherClass()
#ob.func1()
ob.func2()

from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def bank_info(self):
        print("list of bank, SBI, PNB")
    @abstractmethod
    def offers(self):
        print("50% offer for savng scheme")
    @abstractmethod
    def interest(self):
        print("9% yearly interest")

class SBI(Bank):
    def bank_info(self):
        super().bank_info()
        super().offers()
        super().interest()
        print("this is SBI Bank")
    def offers(self):
#        super().offers()
        print("offer as applicable")
    def interest(self):
 #       super().interest()
        print("interest as applicable")

class PNB(Bank):
    def bank_info(self):
        print("this is PNB Bank")
    def offers(self):
        print("offer as applicable within delhi")
    def interest(self):
        print("interest as applicable within delhi")

ob=SBI()
ob.bank_info()
#ob.offers()
#ob.interest()

#ob1=PNB()
#ob1.bank_info()
#ob1.offers()
#ob1.interest()


name=input("enter emp name :")
age=input("enter emp age :")
salary=int(input("enter emp salary :"))

class Employee:
    def __init__ (self,name,age,salary):
        self.name=name
        self.age=age
        self._salary=salary
    
    def show_age(self):
         print("age of the employee is :",self.age)

    def show_name(self):
        print("name of the employee is :",self.name)

class child(Employee):
    def show_salary(self):
        print("salary of the employee is :",self._salary)
        
ob=Employee(name,age,salary)
ob.show_name()
ob.show_age()

ob1=child(name,age,salary)
ob1.show_salary()


account=int (input("enter amount to account"))
amount=int (input("enter amount "))
     
class BankAccount:
    def __init__ (self,account,amount):
        self.account=1000
        self.amount=amount
        
    def depositing(self):
        self.d=(self.account+self.amount)
             
    def withdrawing(self):
        print(self.account-self.amount)
        
    def balance(self):
        print(self.account)

class bank(BankAccount):
    def display(self):
        display("Balance=",self.account)

    def depositing(self):
         print(self.account+self.amount)

    def withdrawing(self):
        print(self.account-self.amount)

    def balance(self):
        super().depositing()
        print(self.account+self.amount)
        
ob=bank(account,amount)
#ob.depositing()
ob.withdrawing()
ob.balance()


class shape:
    def __init__ (self):
        self.name = name

    def rectangle(self):
        l = int(input("Enter rectangle's length: "))
        b = int(input("Enter rectangle's breadth: "))
        rect_area = l * b
        print("The area of rectangle is", rect_area)
        
    def square(self):
            s = int(input("Enter square's side length: "))
            sqt_area = s * s
            print("The area of square is",sqt_area)

    def triangle(self):
        h = int(input("Enter triangle's height length: "))
        b = int(input("Enter triangle's breadth length: "))
        tri_area = 0.5 * b * h
        print("The area of triangle is", tri_area)
 
    def circle(self):
        r = int(input("Enter circle's radius length: "))
        pi = 3.14
        circ_area = pi * r * r
        print("The area of circle is", circ_area)
         
    def parallelogram(self):
        b = int(input("Enter parallelogram's base length: "))
        h = int(input("Enter parallelogram's height length: "))
        para_area = b * h
        print("The area of parallelogram is", para_area)    

class calculate(shape):
    pass

ob=calculate()
ob.rectangle()
'''
         
    
















               
















