'''
x="HELLO WORLD"
print(x)
print(type(x))
print(x[4])
print(x[-1])
print(x[6:11])
print(x[-3:-1])
print(x[:])
print(x[2:])
print(x[:10])
'''
'''
word="HelpA"
print(word[:2])
'''
'''
x="Hello world"
print(len(x))
'''

'''
name="Peter"
age=20
print(name,age)
print("Name of a student is",name,"and the age is",age)
print("Name of a student is " + name + " and the age is "+str(age))
print("Name of a student is %s and the age is %d"%(name,age))
print("Name of a student is {0} and the age is {1}".format(name,age))
'''
'''
str="this is string example";
print(str.capitalize())
print(str.upper())
print(str.lower())
print(str.title())
print(str.swapcase())
print(str.replace('i','L'))
print(str.replace('i','L',1))
'''

'''
str="this is a string"
print(str.count("i"))
print(str.count("i",0,4))
print(str.count("i",5,15))
print(str.find("i"))
print(str.find("is"))
'''

'''
x="hello"
print(x)
print(list(x))
print(tuple(x))
print(set(x))
'''

'''
s=input("type the name")
print(s[0:3])
'''
'''
s=input("type the name")
if(len(s)<3):
 print(s)
else:
 print(s[0:3])
'''
'''
s='This "is" a string'
s1="This is 'a' string"
s3="This 'is' a sting"
print(s)
print(s1)
print(s2)
print(s3)
'''
'''
a=input("type a char to represet no")
c=int (input("type a no to represent char"))
print(ord(a))
print(chr(c))

a="- "
print(a*50)

a=input("entr the test to convert upper case")
print(a.upper())


s=input("Enter the string")
print(s[0:2]+s[-2:])

s=input("Enter the string")
s1=s[1:]
print(s[0]+s1.replace('r', '$'))
'''
s1='abc'
s2='xyz'
s3=s2[0:2]+s1[2]
s4=s1[0:2]+s2[2]
print(s3+" "+s4)


      
