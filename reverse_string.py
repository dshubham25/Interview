
def reverse_string(stack, string):
    stack = []
    for i in range(len(string)):
        stack.push(string[i])
    rev_string = ""
    while not stack.is_empty():
        rev_string += stack.pop()
    return rev_string
