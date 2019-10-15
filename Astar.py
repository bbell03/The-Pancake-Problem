# Caroline Vanderlee and Brandon Bell

def flip(index, stack, aux, num_flips):
    for j in range(5, index, -1):
        a = stack.pop()
        aux.append(a)

    for i in range(index, 5): #
        b = aux[i-index]
        stack.append(b)

    num_flips = num_flips + 1
    # print stack
    return stack

def check_order(stack):
    in_order = True
    for i in range(0, 5):
        if (stack[i] != i+1):
            in_order = False
    return in_order


def find_first_unordered(stack):
    # print('find start')
    for i in range(0, 5):
        if (stack[i] != i+1):
            return i

def count_num_unordered(stack):
    count = 0;
    for i in range(0, 5):
        if (stack[i] != i+1):
            count = count + 1
    return count

#where x is the index of the first unordered pancake
#finds next consecutive element and brings it to the back of the stack
def next_to_end(x, stack, num_flips):
    # print('next start')
    aux = []
    if x == 0:
        for i in range(5): #starting from stack top look for 1 4 elems in
            if stack[i] == 1:
                #pop from 1 to end of stack
                for k in range(5-i):
                    a = stack.pop()
                    # print a
                    aux.append(a)
                # print stack
                # print aux
                for z in range(len(aux)):
                    stack.append(aux[z])
                # print stack
                num_flips = num_flips + 1
                return stack
    elif (not(stack[4] == stack[x-1]+1)):
        # print('in else')
        for i in range(x, 5):
            # print('precondition')
            if stack[i] == stack[x-1]+1:
                # print('postcondition')
                for k in range(5-i):
                    a = stack.pop()
                    # print a
                    aux.append(a)
                # print stack
                # print aux
                for z in range(len(aux)):
                    stack.append(aux[z])
                # print stack
                num_flips = num_flips + 1
                return stack
    else:
        return stack



# Main

stack = []
num_flips = 0

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
    # print(ind)
    # print stack
    stack = next_to_end(ind, stack, num_flips)
    # print stack
    ind = find_first_unordered(stack)
    stack = flip(ind, stack, [], num_flips)
    print stack

print "The spatula was was flipped " + str(num_flips) + " times!"
print "Goal state reached:"
print stack
