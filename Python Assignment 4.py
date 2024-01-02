# Programming Assignment_4
# 1. Write a Python Program to Find the Factorial of a Number?

def fact(num):
    a=1
    for i in range(1,num+1):
        a=a*i
    return a

i=int(input('Enter number'))

print(fact(i))

# 2. Write a Python Program to Display the multiplication Table?

num=int(input('Enter the number'))
for i in range(1,11):
    print(num,"*",i,"=",num*i)
    
# 3. Write a Python Program to Print the Fibonacci sequence?

def fibanci(num):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(3,num+1):
        c=a+b
        print(c)
        a=b
        b=c
        
b=int(input('Enter num'))
fibanci(b)

# 4. Write a Python Program to Check Armstrong Number?


j=int(input('Enter number'))

a=str(j)
b=0
l=len(a)
for i in a:
    b+=int(i)**l
    
if j==b:
    print('Amstrong')
else:
    print('Not Amstrong')
    
# 5.Write a Python Program to Find Armstrong Number in an Interval?
def amstrong(num):
    a=str(num)
    b=0
    l=len(a)
    for i in a:
        b+=int(i)**l
    if num==b:
        print(num)
  
    
   
j=int(input('Enter number'))
for i in range(1,j+1):
    amstrong(i)
    

