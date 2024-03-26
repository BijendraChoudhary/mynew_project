'''
def absolute_value(num):
    if num>=0:
         return num
     else:
        return -num
print(absolute_value.__doc__)
print(absolute_value(2))
print(absolute_value(-4))
'''
'''
def sum(x,y,z):
    result=x+y+z
    return result
print(sum(2,3,4))
'''
'''
x=10
def myfunc():
    x=200
    print(x)
    print("Python")

myfunc()
print(x)
'''
'''
def name(x):
    print(x)
n=input("enter the name:")
name(n)
'''
'''
def add(x,y):
    result=x+y
    print(result)

n1=int(input("enter the first no"))
n2=int(input("enter the second no"))
add(n1,n2)
'''
'''
def sum(x,y):
    result=x+y
    print(result)

n1=float(input("enter the first no"))
n2=float(input("enter the second no"))
sum(n1,n2)
'''
'''
def student(*name):
    print(name)

student('hary','peter',12)
 '''
'''
def student(location="noida",age=25):
 print(age,location)

#student(25,"noida")
student()
'''
'''
def student (**data):
    print(data)
    print(data['name'])    
student(name="peter",age=25,course="MTech",address="Noida")
'''
'''
name=['Johny','Peter','Hary','John']
def student(*name):
 for i in name:
  print(i[1:2])

student(name)
'''
'''
def recur_fact(x):
 if x==1:
  return 1
 else:
  return (x*recur_fact(x-1))
num=int(input("Enter a number :"))
if num>=1:
 print("The fac of",num,"is",recur_fact(num))
'''
'''
#1
x=int(input("enter a no"))
y=int(input("enter another no"))
def add(x,y):
 sum=x+y
 print(sum)

add(x,y)
'''
'''
#x=int(input("enter a no"))
#y=int(input("enter another no"))
def add(x,y=10):
 sum=x+y
 print(sum)

add(3)
'''
'''
def keywordf(i,j,k):
 print("Forst value",i,"second value",k,"third value",j)

keywordf("a","b","c")
'''
'''
def more(**data):
    print("print all inputs",data)

more(Name="Ram", age=10, Qualification="12th")
'''
'''
def fact(x):
 if x==1:
  return 1
 else:
  return(x*fact(x-1))
n=int(input("enter a no to fact "))
if n>=1:
 print("fact",fact(n))
'''
'''
def cal(x,y):
 print((x+y), (x-y))
cal(2,3)
'''
'''
def emp(name,sal=9000):
    print("Name of employee :", name, "and sal is :",sal)

emp("Mohan")
'''
'''
for i in range(4,31):
 if i%2==0:        
  print("Even",i)
 else:
  print("Odd",i)           
'''
'''
list=[1,2,3]
def mul():
 print(list[0]*list[1]*list[2])
mul()
'''
'''
a=input("enter name")
def up():
 print(a.upper())
up()
'''





