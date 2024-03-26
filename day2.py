'''
import math
x=int(input("Enter the No"))
a=int(x%10)
b=int((x/10)%10)
c=int((x/100)%10)
d=int((x/1000)%10)
e=int((x/10000)%10)
sum=(a+b+c+d+e)
print(sum)
'''

'''
x=100
print(type(x))
print(x)

y=float(x)
print(y)
'''
'''
import math
x=str (input("Enter first No"))
y=str (input("Enter second No"))
sum=(x+y)
prod=int(x*y)
print(sum)
print(prod)
'''

'''
x={1,2,3,10,5,0}
print (list(x))
print (tuple(x))
print (set(x))
print(set(x))
'''
'''
import math
a=float (458.546315)
print (round (a,2))
print (round (a,-2))
'''

'''
x=[1,2,3]
if(2 in x):
 print("Yes, it is")
else:
 print('No')
#print("No")
#print(2 not in x)
'''

'''
#Q1
list=[23,25,17,97,43]
print(max(list))
'''

'''
#Q2
list=(34,23,63,12)
print(min(list))
'''

'''
#Q3
n=int(input("Type first no : "))
if(n%2==0):
 print("Even No")
else:
 print("Odd No")
'''



'''
#Q4
s=('John','Peter','Hary','Davik','Stephen')
if('John' in s):
 print("Yes")
else:
 print("No")
'''

'''
#Q5
L1=["hello", 56, 98.7]
L2=["hello", 56, 98.7]
print(L1 is L2)
'''
'''
#Q6
s=input("Enter the string")
print(s*5)
'''

'''
#Q7
x=input("Enter the first string")
y=input("Enter the first string")
sum=x+y
print(sum)
'''

'''
#Q8
s=input("Enter the string")
print(s*50)
'''

'''
#Q9
n1=int (input("Enter a No"))
n1+=100
print(n1)
'''
import math
a=102.34
print(math.floor(a))
print(math.ceil(a))
