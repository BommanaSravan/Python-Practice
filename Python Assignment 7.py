# 1. Write a Python Program to find sum of array?

l=[1,2,4,5,6,78,5]

A=lambda X,y : X+y

from functools import reduce

b=reduce(A,l)
print(b)

# 2. Write a Python Program to find largest element in an array?

l = [1,2,3,-412, 123, 369, 111]

r=0
for i in l :
    if i>r:
        r=i
print(r)

# 3. Write a Python Program for array rotation?

l = [1,2,3,-412, 123, 369, 111]

print(l[::-1])

# 4. Write a Python Program to Split the array and add the first part to the end?

l=[1,2,3,5,5,6,7,8]

print(len(l))

l1=l[:int(len(l)/2)]
l2=l[int(len(l)/2):]


print(l2.extend(l1))
