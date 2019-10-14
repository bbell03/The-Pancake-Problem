# Caroline Vanderlee and Brandon Bell

def flip(index, stack, aux):
    for j in range(5, index, -1):
        a = stack.pop()
        aux.append(a)

    for i in range(index, 5): #
        b = aux[i-index]
        stack.append(b)

    return stack

def check_order(stack):
    in_order = True
    for i in range(0, 5):
        if (stack[i] != i+1):
            in_order = False
    return in_order


def find_first_unordered(stack):
    print('find start')
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
def next_to_end(x, stack):
    print('next start')
    aux = []
    if x == 0:
        for i in range(5): #starting from stack top look for 1 4 elems in
            if stack[i] == 1:
                #pop from 1 to end of stack
                for k in range(5-i):
                    a = stack.pop()
                    print a
                    aux.append(a)
                print stack
                print aux
                for z in range(len(aux)):
                    stack.append(aux[z])
                print stack
                return stack
    else:
        print('in else')
        for i in range(x, 5):
            print('precondition')
            if stack[i] == stack[x-1]+1:
                print('postcondition')
                for k in range(5-i):
                    a = stack.pop()
                    print a
                    aux.append(a)
                print stack
                print aux
                for z in range(len(aux)):
                    stack.append(aux[z])
                print stack
                return stack

#def is_consecutive(stack):
    #i = -1
    #for i in range(0, 4):
        #if ((stack[i] == stack[i+1] - 1) or (stack[i] == stack[i+1] + 1)):
            #return i


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

while(not(check_order(stack))):
    ind = find_first_unordered(stack)
    print(ind)
    print stack
    stack = next_to_end(ind, stack)
    ind = find_first_unordered(stack)
    stack = flip(ind, stack, [])
    print stack


    #recurse_flip(ind, stack)


print "Goal state reached:"
print stack
