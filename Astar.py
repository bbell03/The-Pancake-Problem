# Caroline Vanderlee and Brandon Bell

stack = []
aux = []
goal = [1, 2, 3, 4, 5]

print "Enter the pancake stack (5 integers from 1 to 5):"

for i in range(0, 5): 
        ele = int(input()) 
        stack.append(ele)
      
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

# Is the stack out of order?
out_of_order = False
for i in range(0, 5):
        if (stack[i] != i+1):
                out_of_order = True

if (out_of_order):
        print "Out of order!"
else:
        print "In order!"


# x = stack.pop()
# print x
# print stack
# stack.append(x)
# print stack