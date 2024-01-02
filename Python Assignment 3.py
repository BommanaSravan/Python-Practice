# 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

a=int(input('Enter the number'))

if a>0:
    print('Enter the number is positive')
elif a<0:
    print('Enter the number is Negative')
else:
    print('Enter the number is zero')
    
# 2. Write a Python Program to Check if a Number is Odd or Even?

a=int(input('Enter the number'))

if a%2==0:
    print('Enter the number is even')
else:
    print('Enter the number is odd')
    
 # 3. Write a Python Program to Check Leap Year?

a=int(input('Enter the year'))

if a%100==0 and a%4==0 :
    print('Leap year')
elif a%4==0:
    print('Leap Year')    
else:
    print('Not leap year')    
    
    
# 4. Write a Python Program to Check Prime Number?

a=int(input('Enter the number'))

c=0
if a>0:
    for i in range(1,a+1):
        if a%i==0:
            c=c+1
    
if c==2:
    print('Prime Number')
else:
    print('not prime')
    
# 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?          
def prime(num):
    c=0
    for i in range(1,num+1):
        if num%i==0:
            c=c+1
    if c==2 and num !=1:
        print(num)
        
a=int(input('Enter the number'))        
for i in range (a+1):
    prime(i)            
       
        