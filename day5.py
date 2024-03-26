'''
x=(1,23.7,'python',[1,2,3])
print(type(x))
print(x[2])
print(x[3])
print(x[3][2])
'''
'''
x=(1,23.7,'python',(1,2,3),[89,67,'hello'])
#print(type(x))
#print(x[4][0])
#x[1]=2000
#print(x)
#x[3][0]=900
x[4][0]='hello'
print(x)
'''
'''
t=(45,67,87,45,53,45)
print(t.count(45))
print(t.index(45,4,6))
print(max(t))
print(min(t))
print(len(t))
print(sum(t))
'''
'''
t=(45,67,87,45,53,45)
print(sorted(t))
print(sorted(t,reverse=True))
print(t[::-1])
'''
'''
x=int (input("Enter the No"))
if(x>100):
    print(x,"Yes %d it is greater " %(x))
elif(x==100):
    print(x,"%d No is equal to 100" %(x))
elif(x>5):
    print(x,"%d No is greater than 5" %(x))
else:
    print(x,"%d No is smaller than 100" %(x))


x=int (input("Enter the No"))
if(x<200):
    print("Yes %d it is smaller than 200 " %(x))
    if(x==100):
     print("%d No is equal to 100" %(x))
    #else:
     #print("%d No is greater than 50" %(x))
else:
 print("%d No is greater than 100" %(x))

x=0
while(x<9):
 print(x)
 x+=1
else:
 print (x,"is not less than 9")

x=10
for i in range(x):
 #print(i)
 print(i,end=" ")

x=[1,23.7,'python',(1,2,3),[89,67,'hello']]
for i in x:
 print(x.index(i),i,end=" \n")


#1 sum all the items in a list
x=[1,2,3]
print(sum(x))

#2 and 3 get the largest/smallest number from a list
x=[1,2,3]
print(max(x))
print(min(x))


# 4 display the first and last colors from the fw list.
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0], color_list[-1])


#5
x=input("enter the string")
if ('ing' in x):
    print(x+'ly')
else:
    print(x+'ing')

a=int (input("marks of sub one"))
b=int (input("marks of sub one"))
c=int (input("marks of sub one"))
d=int (input("marks of sub one"))
e=int (input("marks of sub one"))
sum=(a+b+c+d+e)
per=(sum/5)
print(sum)
print(per)
if(per>=60):
    /*-print("First Division")  890-e0/    print("Third Division")
else:
    print("Fail")


a=int (input("enter the no"))
b=int(input("enter the no"))
c=int(input("enter the no"))
d=[a,b,c]
print(max(d))


a=int (input("Enter the year"))
if(a%4==0):
 print("Leap Year")lislist1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]t1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
else:
 print("Non leap year")
'''


#11
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# Sub List to be added = ["h", "i", "j"]
#list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

'''
i=0
while(i<10):
 print(i)
 i=i+1
 '''

'''
i=0
for i in range(10):
 print(i)
'''
'''
list1=[12,4,490]
for i in range (len(list1)):
 print(i," ", list1[i])
 '''

'''
i=0
while(i<9):
 print(i)
 i=i+1
 if(i==3):
  break
'''
'''
for i in range(1,8,2):
 print(i)
'''
'''
x=0
while(x<7):
    x=x+1
    if(x==3):
        break
        #continue
    print(x)
'''

'''
i=0
for i in range(7):
 if(i<7):
  print(i)
  continue
'''
'''
for num1 in range(1):
    for num2 in range(2):
        for num3 in range(3):
         print(num1, ':', num2, ':',num3)
'''

'''
x={}
#print(type(x))
#x={1:23,5:89}
#x={1:"Hellow",8:69.67}
x={1:"hello","Ok":[1,2,3,4,5]}
#print(x)
#print(x.keys())
#print(x.values())
x[1]="Python"
print(x)
'''
'''
x=dict([(1,23),(2,45),("Hello","cdac")])
print(x)
print(x.keys())
print(x.values())
print(x[1])
print(x["Hello"])
'''
'''
x={1:23,4:"cdac","location":"noida"}
#x["location"]="pune"
#x.update({'course':'python'})
x[56]=800
print(x)
'''
'''
dict1={1:34,5:67,9:87}
dict2={"name":"cdac","location":"Noida"}
#dict1.update(dict2)
#print(dict1)
#print(dict1.pop(1))
#print(dict1.popitem())
#print(dict1)
del dict1
print(dict1)
'''
'''
x={}.fromkeys(['math','science'],90)
x=[eng:90]
x.update('eng')
print(x)
'''
'''
a={1,2,3,4,5}
b={4,5,6,7,8}
#print(a|b)
#print(a.union(b))
#print(a.intersection(b))
#print(b.difference(a))
#a.add(9)

print(a.symmetric_difference(b))
'''
















































