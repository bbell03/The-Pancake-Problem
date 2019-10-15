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
    # increment the number of flips
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
    # if 1 is the first element out of order and not last on the stack
    # flip from stack at that point: choose that ordering as leaf node
    if x == 0 and (not(stack[4] == 1)):
        for i in range(5):
            if stack[i] == 1:
                # flip the stack from that point
                for k in range(5-i):
                    a = stack.pop()
                    aux.append(a)
                for z in range(len(aux)):
                    stack.append(aux[z])
                # increment the number of flips and print the stack
                num_flips = num_flips + 1
                print stack
                return stack
    # if the first element out of order is not the last element on the stack
    # and 1 is not the last element on the stack:
    elif (not(stack[4] == stack[x-1]+1)) and (not(stack[4] == 1)):
        for i in range(x, 5):
            # find elements out of order
            # permutations of flipping of the stack from each element are added to the frontier
            # choose the next unordered element to flip from:
            # choose that permutation leaf node from the frontier
            if stack[i] == stack[x-1]+1:
                # flip the stack from that point
                for k in range(5-i):
                    a = stack.pop()
                    aux.append(a)
                for z in range(len(aux)):
                    stack.append(aux[z])
                # increment the number of flips and print the stack
                num_flips = num_flips + 1
                print stack
                return stack
    # otherwise (1 is the last element on the stack):
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

# while loop for A*
# initialize frontier with initial state: stack
# while the goal state has not been reached
while(not(check_order(stack))):
    # choose the first unordered element: choose that permutation as leaf node
    # put unordered element at the end
    ind = find_first_unordered(stack)
    stack = next_to_end(ind, stack)
    # flip the stack so that the unordered element is in order
    ind = find_first_unordered(stack)
    stack = flip(ind, stack, [])
    # return stack at that point
    print stack

print "The spatula was was flipped " + str(num_flips) + " times!"
