'''
x={1,2,3,"hello"}
x.add(700)
#x.remove("hello")
y=frozenset(x)
#y.append(5)
#y.remove(700)
x.discard(1)
print(x)
'''
'''
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
out=color_list_1-color_list_2
print(out)
'''
'''
i=0
for i in range(7):
 print('*' * i)
'''
'''
#Q1
no1=int (input("Enter a no : "))
no2=int (input("Enter another no : "))
cal=no1*no2
print(cal)
'''

'''
#2Display float number with 2 decimal places
Num=float (458.541315)
print(round(Num,2))
'''
'''
#3 I have 500 rupees so I can buy 5 flowers for 80 rupees.
TotalAmount=500
Price=80
Quantity=5
#print("I have", TotalAmount,"rupees so I can buy", Quantity,"flowers for",Price,"rupees.")
print(("I have, {0},rupees so I can buy, {1},flowers for,{2} rupees ").format(TotalAmount,Quantity,Price))
'''
'''
list=[10,20,100,125,5,150,200]
for i in range(len(list)):
 if(list[i]>=150):
  continue
 print(list[i])
'''
'''
list=[10,20,100,125,600,150,200]
for i in range(len(list)):
 if(list[i]>500):
  break
 print(list[i])
'''
'''
a=[1,2,3,4,5,6,7,8,9,10]
print(a[::-1])
'''
'''
i=0
list=[3,4,5,15,20]
if(i<5):
  (list[i]<=5)
  i=i+1
print(list[i])
else:
  print("All done")
'''
'''
#hehalloweenllo
list1="hello"
list2="halloween"
print(list1[0:2]+list2+list1[2:5])
'''
'''
i=1
while (i<=10):
    print(i)
    i=i+1
'''
'''
i=11
while (i>1):
    i=i-1
    print(i)
 '''

    
   
