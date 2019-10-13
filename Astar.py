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

def find_first_unordered(stack):
    for i in range(0, 5):
        if (stack[i] != i+1):
            return i

stack = []
aux = []

print "Enter the pancake stack (5 integers from 1 to 5)."
print "Press enter after each number. Enter the stack from bottom to top."

for i in range(0, 5):
        ele = int(input())
        stack.append(ele)

print "Your stack is, from bottom to top:"
print stack

if(not(check_order(stack))):
    ind = find_first_unordered(stack)
    print "First unordered index: " + str(ind)
    print "Flipping: "
    flip(ind, stack, aux)


print "Goal state reached:"
print stack
