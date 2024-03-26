'''
list1=[12,3,4,"hello"]
list2=["world",100]
print(list1+list2)
print(list2*2)
'''
'''
x=[12,3.4,"hello",[56,34],100]
#print(type(x))
#print(x[3][1])
#x[3][0]="python"
print(x)
x[3][1]="Z"
print(x)
'''
'''
x=[12,3.4,"hello",[56,34],100]
print(x[0:])
'''
'''
x=[12,3.4,"hello",[56,34],100]
x.append("world")
print(x)
x.append([800,500])
print(x)
x.extend([800, 1000])
print(x)
'''
'''
x=[100,'hello','python',700]
x.insert(2,'cdac')
print(x)
print(x[2])
print(x[3])
'''
'''
x=[100,200,'abc','xyz']
print(x)
del x[1]
print(x)
del x
print(x)
'''
'''
x=[100,200,'abc','xyz']
x.remove(200)
print(x)
'''
'''
x=[23,56,2,23,61,90]
x.sort()
print(x)
#x.sort(reverse=True)
x.reverse()
print(x)
print(max(x))
print(min(x))
print(len(x))
'''
'''
x=['hello','cdac','in','noida']
print(ord('h'))
print(ord('c'))
print(ord('i'))
print(ord('n'))
print(max(x))
print(min(x))
x.sort()
print(x)
'''
'''
x=[100,300,'abc',100,'xyz',100,'abc']
print(x.count(100))
print(x.count('xyz'))
print(x.index('xyz'))
'''
'''
x=[100,300,'abc',100,'xyz',100,'abc']
print(x)
print(x.clear())
'''
'''
x=[10,20,'hello',[200,300,['abc','xyz'],5],125]
print(x[3][2][1])
'''
'''
x=[100,200,300,100,'Python']
#print(x.find(100))
print(x.index(100,3))
'''
'''
x=[10,20,'hello',[200,300,['abc','xyz'],5],125]
print(x)
x[3][2][1]=1000
print(x)
 '''
'''
#1 Find the max number from the list
x=[23,56,81]
print(max(x))
'''

'''
#2 Finth the minimum value
x=["Hello","help","Held"]
#print(ord('H'))
#print(ord('h'))
#print(ord('H'))
print(min(x))
'''
'''
#3 reverse the list
x=[23.67,76.21,89,900,56.3]
x.reverse()
print(x)
'''
'''
#4 descending order
x=[23.67,76.21,89,900,56.3]
x.sort(reverse=True)
print(x)
'''
'''
#5 to print 78 and 'world'
x=[12,54,98,"help",[12,45,78,['hello','world']]]
print(x[4][2])
print(x[4][3][1])
'''

'''
#6 Replace 45(Q.5) with 'PYTHON'
x=[12,54,98,"help",[12,45,78,['hello','world']]]
x[4][1]="PYTHON"
print(x)
'''
'''
#7 add "CDAC","Noida" as two elements 
x=[12,34,67,32]
#x.append(["CDAC", "Noida"])
x.append('CDAC')
x.append('Noida')
print(x)
'''
'''
# 8 add a new list
x=[12,34,67,32]
x.append(["CDAC", "Noida"])
print(x)
'''
'''
#9 find the index number of the third
#occurence of 'zara'
x=[12,'zara','xyz',45,78.8,'zara','100','zara']
#print(x.find('zara'))
#print(x.index('zara',6,8))
#print(x.index('zara',6, len(x)))
print(len(x))
'''
'''
#10 insert a new item(i.e ABC) at index 4
x=[12,'zara','xyz',45,78.8,'zara','100','zara']
x.insert(4,'ABC')
print(x)
'''

