# Caroline Vanderlee and Brandon Bell

def flip(index, stack, aux):
    for j in range(5, index, -1):
        a = stack.pop()
        aux.append(a)

    for i in range(index, 5):
        b = aux[i-index]
        stack.append(b)

def check_order(stack):
    in_order = True
    for i in range(0, 5):
        if (stack[i] != i+1):
            in_order = False

    return in_order

stack = []
aux = []

print "Enter the pancake stack (5 integers from 1 to 5)."
print "Press enter after each number. Enter the stack from bottom to top."

for i in range(0, 5):
        ele = int(input())
        stack.append(ele)

print "Your stack is, from bottom to top:"
print stack


# Test flip
print "Pop 3 elements off the stack"

num = 3;

ind = num-1;
flip(ind, stack, aux)

print stack

# Is the stack out of order?

if (check_order(stack)):
        print "In order!"
else:
        print "Out of order!"


# x = stack.pop()
# print x
# print stack
# stack.append(x)
# print stack
