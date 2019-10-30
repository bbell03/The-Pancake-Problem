# A Pancake Problem
###### COMP 131: Artificial Intelligence
###### Homework 2: A* Search
###### Tufts University

# README

### Author(s): Kerem San and Brandon Bell

### CODE DETAILS

  ### IMPLEMENTATION:
    We expect that our solution has been completely and correctly implemented
    This code was written in Python 2.7.8

  ### ARCHITECTURE:
    Our solution makes use of modularity and object oriented design to
    order a stack of pancakes using the A* search algorithm.

    All functions take a stack as an input, and return either its various
    relevant attributes or the stack itself.

  #### FUNCTION(S) IMPLEMENTED INCLUDE:

    flip(index, stack, aux)
      * takes an index, a stack and an auxiliary and flips the stack from from
      the index to the end, using the auxiliary stack to hold intermediary data.

    check_order(stack)
      * takes a stack and returns a boolean value according to whether the
      the stack is in consecutive order from 1-5

    find_first_unordered(stack)
      * takes a stack and returns the index of the first element not in
      consecutive order from 1-5

    count_num_unordered(stack)
      * takes a stack and returns the number of elements out of consecutive
      order from 1-5

    next_to_end(x, stack)
      * takes a stack and flips a substack from the next consecutive element to
      the end of the stack so that the next element is at the end.

  ### METHODOLOGY:
    Our program is implemented according to the A* search algorithm described
    in the specification and class slides. In our implementation, the main
    function is characterized by a while loop that repeatedly finds the next
    consecutive element, brings it to the end of the stack and then flips a
    substack from the first element out of order to the end, ensuring that the
    next consecutive element, which is now at the end, is put in its proper
    order. Our heuristic function was the amount of pancakes out of order.
    Our cost function was how many times we would flip the spatula to put
    the next element in order. Cost was minimized by finding the next element
    out of order and directly putting that in order, as opposed to flipping
    other elements to eventually put that element in order. Leaf nodes are
    represented by different stack orderings where orders alternate between
    the next ordered element being at the end (i.e. one flip away from being
    ordered) and then brought to its proper place (i.e. ordered, lowering the heuristic).
