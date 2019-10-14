# Caroline Vanderlee and Brandon Bell

# helper function flip
def flip(index, stack, aux):
    for j in range(5, index, -1):
        a = stack.pop()
        aux.append(a)

    for i in range(index, 5): #
        b = aux[i-index]
        stack.append(b)


# helper function check_order
def check_order(stack):
    in_order = True
    for i in range(0, 5):
        if (stack[i] != i+1):
            in_order = False
    return in_order


# helper function find_first_unordered
def find_first_unordered(stack):
    for i in range(0, 5):
        if (stack[i] != i+1):
            return i


# helper function count_num_unordered
def count_num_unordered(stack):
    count = 0;
    for i in range(0, 5):
        if (stack[i] != i+1):
            count = count + 1
    return count


# helper function brandon_flip
def brandon_flip(index, stack, aux):
    for j in range(5-index, index, -1):
        a = stack.pop()
        aux.append(a)

    for i in range(index, 5-index): #
        b = aux[i-index]
        stack.append(b)


# helper function is_consecutive
def is_consecutive(stack):
    i = -1
    for i in range(0, 4):
        if ((stack[i] = stack[i+1] - 1) or (stack[i] = stack[i+1] + 1))
            return i


# helper function recurse_flip
def recurse_flip(ind, stack):
    flip(ind, stack, [])
    if(not(check_order(stack))):
        ### ALGORITHM FOR CALCULATING INDEX TO FLIP GOES HERE ###
        ind = find_first_unordered(stack) + 1 # placeholder: must change
        #recurse_flip(ind, stack)


# Main

stack = []

print "Enter the pancake stack (5 integers from 1 to 5)."
print "Press enter after each number. Enter the stack from bottom to top."

for i in range(0, 5):
    ele = int(input())
    stack.append(ele)

print "Your stack is, from bottom to top:"
print stack

if(not(check_order(stack))):
    ind = find_first_unordered(stack)
    recurse_flip(ind, stack)


print "Goal state reached:"
print stack
