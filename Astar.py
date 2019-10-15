# Caroline Vanderlee and Brandon Bell

# variables needed
stack = []
num_flips = 0


# helper function flip
# flips the stack at a given index
def flip(index, stack, aux):
    for j in range(5, index, -1):
        a = stack.pop()
        aux.append(a)

    for i in range(index, 5):
        b = aux[i-index]
        stack.append(b)

    # increment number of flips
    global num_flips
    num_flips = num_flips + 1

    return stack


# helper function check_order
# checks if the stack is out of order
def check_order(stack):
    in_order = True
    for i in range(0, 5):
        if (stack[i] != i+1):
            in_order = False
    return in_order


# helper function find_first_unordered
# finds the first unordered element in the stack
def find_first_unordered(stack):
    for i in range(0, 5):
        if (stack[i] != i+1):
            return i


# helper function count_num_unordered
# counts the number of elements out of order in the stack
def count_num_unordered(stack):
    count = 0;
    for i in range(0, 5):
        if (stack[i] != i+1):
            count = count + 1
    return count


# helper function next_to_end
# finds the next element out of order in the stakc
# and brings it to the end (here the top) of the stack
def next_to_end(x, stack):
    global num_flips
    aux = []
    if x == 0:
        for i in range(5):
            if stack[i] == 1:
                for k in range(5-i):
                    a = stack.pop()
                    aux.append(a)
                for z in range(len(aux)):
                    stack.append(aux[z])
                num_flips = num_flips + 1
                print stack
                return stack
    elif (not(stack[4] == stack[x-1]+1)):
        for i in range(x, 5):
            if stack[i] == stack[x-1]+1:
                for k in range(5-i):
                    a = stack.pop()
                    aux.append(a)
                for z in range(len(aux)):
                    stack.append(aux[z])
                num_flips = num_flips + 1
                print stack
                return stack
    else:
        return stack


# Main

print "Enter the pancake stack (5 integers from 1 to 5)."
print "Press enter after each number. Enter the stack from bottom to top."

for i in range(0, 5):
    ele = int(input())
    stack.append(ele)

print "Your stack is, from bottom to top:"
print stack
num_unordered = count_num_unordered(stack)
print "There are " + str(num_unordered) + " elements out of order in this stack."

while(not(check_order(stack))):
    ind = find_first_unordered(stack)
    stack = next_to_end(ind, stack)
    ind = find_first_unordered(stack)
    stack = flip(ind, stack, [])
    print stack

print "The spatula was was flipped " + str(num_flips) + " times!"
