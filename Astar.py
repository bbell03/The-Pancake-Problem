# Caroline Vanderlee and Brandon Bell

stack = []
aux = []

print "Enter the pancake stack (5 integers from 1 to 5):"

for i in range(0, 5): 
        ele = int(input()) 
  
        stack.append(ele) # adding the element 
      
print(stack) 


# Test flip
print "Pop 3 elements off the stack"

n = 3

for j in range(5, n-1, -1):
        a = stack.pop()
        aux.append(a)

print aux

for i in range(n-1, 5):
        b = aux[i-n+1]
        stack.append(b)

print stack


# x = stack.pop()
# print x
# print stack
# stack.append(x)
# print stack