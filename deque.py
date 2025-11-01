''''
What happens if you try to pop from an empty deque?
it raises an index error

Why is deque faster than using a Python list for stack operations?
it is optimized for fast appends and pops from both ends making it ideal for stack operations

Write a method to reverse a string using a deque stack.
'''
'''
from collections import deque

def reverse_string(s):
    stack = deque()

    # Push all characters onto the stack
    for ch in s:
        stack.append(ch)

    
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()

    return reversed_str


# Example
print(reverse_string("idhil"))






#How can you limit the stack size using deque(maxlen=N)?
#you can set a maximum size for deque

#Implement a function that checks for balanced parentheses using deque.
'''

from collections import deque

def is_balanced(expr):
    stack = deque()
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in expr:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack

# Example
print(is_balanced("{[a*(b+c)]+(d/e)}"))  
print(is_balanced("{[a*(b+c])}"))       

