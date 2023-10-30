import sys # for using command-line arguments

my_list = ["welcome", "to", "python"]

def max_val(num_list : list[int]) -> int:
    '''
    returns the maximum value from num_list

    Params:
    num_list: a list of numbers

    Returns:
    the maximum from num_list
    '''
    # python is whitespace sensitive (newlines and indentation matter!)
    max_val = num_list[0] # TODO: handle the case where num_list is empty
    for num in num_list: # for (int num: num_list)
        if num > max_val: # executes inside of the for-loop
            max_val = num # executes inside of the if
    return max_val # executes outside of the for-loop

# command-line arguments live in sys.argv, with index 1 being the 
# first one
print(sys.argv[0]) # will print name of file
if (len(sys.argv) > 1):
    print("You gave me: " + sys.argv[1])

pass # a command that has no effect 
# debuggers stop before the last line