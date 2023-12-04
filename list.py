#list 
# list is the data type which is used to store multiple values in single variable 
# ordered 
# changeble 
# accept duplicate values 
# listname = [list of varibles]
# eg list1 = ["ram","shyam","hari",20]
# eg list2 = ["nishan" "age"]
'''name = ["nishan","hari",23,12,"sita",'hari']
print(name)'''
#indexing and slicing 
#indexing is the processing of finding specific element from given sequence (string,list,tuples)
#name = 'nishan shrestha'
# from postive indexing we can count from n and negative indexing we can count from a 
#slicing 
#process of finding subset of given sequence. it occur from the range 
#eg 
#a = "hello i love programming"
# print(a[::-1]) reverse print 1:(to) 4 (within)
#let suppose 1:3:5 here 5 is the gap between first (1) and last(3)
'''pname = 'NEPAL'
print(pname)
print(pname[0:4])
print(pname[0:3])
print(pname[0:2])
print(pname[0:1])'''
#or we can print(pname[::-1])
'''nishan = 'NEPAL'
print(nishan[0:5])
print(" "*1+nishan[1:5])
print(" "*2+nishan[2:5])
print(" "*3+nishan[3:5])
print(" "*4+nishan[4:5])'''
'''n = "kathmandu"
print(" "*4+n[1:-7])
print(" "*3+n[3:-3])
print(" "*2+n[2:-3])
print(" "*1+n[0:-1])
print(n[0:9])'''
'''n = 5 
for i in range(0,n):
  for j in range(n,i-1):
   print("*",end = '')
print()'''

'''hello = "*****"
print(hello[0:5])
print(hello[0:4])
print(hello[0:3])
print(hello[0:2])
print(hello[0:1])'''

'''n =5 
for i in range(0,n+1):
 for j in range(0,i-1):
  print("*",end = " ")
 print()'''

'''hi = "KATHMANDU"
print(hi[0:9])
print(" "*1+hi[1:8])
print(" "*2+hi[2:7])
print(" "*3+hi[3:6])
print(" "*4+hi[4:5])'''
'''oe = "**"
hello ="NEPAL"
hi = "**"
print(oe+hello[0:5]+hi)
print(oe+hello[0:4]+hi)
print(oe+hello[0:3]+hi)
print(oe+hello[0:2]+hi)
print(oe+hello[0:1]+hi)'''
'''me = ["hari","shyam","c","d","e",3]
print(me.append("nishan"))# it takes it type rather than added'''
# me.append("nishan")
#print(me)
'''hello = ["hari","shyam","c","d","e",3]
hello.insert(2,"nishan")
print(hello)'''
'''b =['ram',"shyam","hari"]
b.insert(1,"nishan") # insert takes two argument 
print(b)'''

'''b =['ram',"shyam","hari"]
b.append("nishan")# append takes 1 argument 
print(b)'''

'''b =['ram',"shyam","hari"]
b.pop(1)# b.pop() last element will automatically reomove
print(b)'''
'''hi_nishan = ["nishan","nishan", "nishan", "gita"]
hi_nishan.remove("nishan")
hi_nishan.remove("nishan")
hi_nishan.remove("nishan")
print(hi_nishan)'''

'''hi_nishan = ["nishan","hari","gita","parbati"]
hi_nishan.insert(0,"hello")# by inserting we can remove the list string and put from insert value
print(hi_nishan)'''
from bisect import insort
from multiprocessing import Condition
import re


'''a = [1,23,445,545,566,344]
a.sort(reverse=False)
print(a)'''


'''nishan = ['aeroplane4w',"aeroplaeww","aeroplqwe","aeroplane4x"]
nishan.sort()
print(nishan)'''

'''name_list = [23,34,566,78,999,455,567]
number = map(lambda x:x**2,name_list)
print(list(number))'''

#map function in python 
'''number1  = [12,223,45,56,67]
number2 = [23,456,5677,567,543]
number = map(lambda x,y:x+y,number1,number2)
print(list(number))'''

#tuples 
#used to store multiple variable in single variable 
# ordered
# unchangable 
# accept dublicate values
#tuple are created by the using round bracket() or the parenthesis ().


'''names = ("nishan","hari","shyam","anil","shyam"," nothing")
#print(names[1:3])
name = list(names)
name.append("hello_there")
name = tuple(name)
print(name)'''

#write the python program to  create the folling tuples:
'''birds = ("parrot","crow","hen")
bird = list(birds)
bird.append("cow")
print(bird)'''


'''bird1 =["hen","parrot","kiwi","parrot"]
bird1.extend("nishan")
print(bird1)'''

'''bird1 = ("kiwi","crow","parrot","a","b",'c')
bird2 = ('baknd',"nsihab","sbaki","swu")
bird3 = ("dnks","snsk","dfndk")
bird4 = bird1+bird2+bird3
print(bird4)'''

# if else statement 
#syntax 
'''if Condition:
    # write a statement 
else:
      #statement  
                        '''
# write a program to cheak wheather she vote or not 

'''age = eval(input("enter the age of person:"))
if age >= 18:
    print("He/she can vote ")
else:
    print("he/she cannot vote")'''
'''a = input("enter the name of the person:")
b = eval(input("enter the age:"))
if b >= 18:
     print("He/she can vote ")
else:
    print("he/she cannot vote")
print(a,b,"is eligible to vote")  '''

#write a program to cheak smallest number between them 
# 4 variable comparision 
# find the squre and cube of given number:
'''a = eval(input("enter the first number:"))
print("the squre of given number is",a**a)
cube = a**3
print(cube)'''


'''number = eval(input("enter the any number:"))
if number%2 == 0:
   print("the given number is even")
else:
  print("the given number is odd")'''

'''a = eval(input("enter the any number:"))
if a >0:
    print("a is positive")
elif a==0:
   print("the number is zero")
else:
    print("the number is negative")'''







