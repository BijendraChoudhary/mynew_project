
'''
#Q1 to add all the odd numbers from 0 to 20
i=1
for j in range(20):
 i=i+j
 j=j+2
print(i)
'''
'''
#Q2 sum of all integers greater than 100 and less than 200.
i=0
for j in range(100,200):

     i=i+j #0+100=100
     j=j+1
print(i)
'''
'''
 #Q3 sum of square of the first ten even natural numbers
j=0
for i in range(2,11):
#while(i<10):
 #i=i+2
#print((i), 'x',(i)) 
 if(i%2==0):
  i=i*i
 print(i)
 j=j+i
print(j)
'''
'''
#Q4
for i in range(65,91):
 print(chr(i))
'''

'''
#5Display ascii characters from 48 to 57
for i in range(48,57):
 print(chr(i))
'''
'''
#5Display ascii characters from 48 to 57
for i in range(97,123):
 print(i ,chr(i))
'''
'''
#Q7
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic=dic1|dic2|dic3
#dic.update(dic3)
print(dic)
#dic=dic.update(dic3)
#print(dic)
'''
#Q8 to add in {2: 30}
dict={0: 10, 1: 20}
#dict.update({2:30})
dict[2]=30
print(dict)



















