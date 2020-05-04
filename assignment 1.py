import math

# 2nd  question

for i in range(2000,3201):
   if (i%7==0 and i%5!=0):
       print(i,end=",")
            
question 3

            
x=input("Enter first")
y=input("Last name")

reverse=(x+" "+y)[::-1]
print(reverse)    
    
#question 4

d=12
r=d/2*(10**(-2))
V=(4/3)*(math.pi)*(r**3)         
print("The volume of the given Sphere is", V , " cubic meter")    
            
# Task 2

#question 1
accept=input(" enter comma separated values ")
list=accept.split(",")
print(list)

#question 2
for i in range(9):
    if (i <6):
     for j in range(i):
        print("*"*j)
     else:
       for j in range(i):
            print('*'*(i-j))
    
#question 3:
word=input("please enter the word bro:")
reverse2=word[::-1]   
print(reverse2)
           