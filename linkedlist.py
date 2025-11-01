#Modify the StackLinkedList to support a clear() method.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return "Stack is empty!"
        popped = self.top.data
        self.top = self.top.next
        return popped

    def clear(self):
        self.top = None
        

# Example
stack = StackLinkedList()
stack.push(10)
stack.push(20)
stack.clear()
print(stack.top)  


#How can you detect memory leaks in a linked list stack implementation?
#by using garbage collector module to find uncollected objects

#What would happen if you forget to update self.top after popping?
#the top element wont be removed automatically 

#Implement an __iter__() method to traverse the stack from top to bottom.
'''
class StackLinkedList:
    # (previous methods same as before)

    def __iter__(self):
        current = self.top
        while current:
            yield current.data
            current = current.next

# Example
stack = StackLinkedList()
stack.push(10)
stack.push(20)
stack.push(30)

for item in stack:
    print(item)

#Compare the space complexity of deque vs Linked List.
#they both use time space of O(n) but linked list has a higher memory overhead
'''