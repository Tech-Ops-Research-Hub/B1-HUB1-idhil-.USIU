#Implement a queue using only two stacks in Python or JavaScript.
from collections import deque 
class QueueUsingStacks:
    def __init__(self):
        stack1 = deque()
        stack2 =deque()

    def enqueue(self,item):
        self.stack.append(item)   

    def dequeue(self,):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack2.pop()) 
        if not self.stack2:
            return "stack is empty" 
        return self.stack.pop()  
             
    def is_empty(self):
          return not self.stack1 and not self.stack2

    def size(self):
        return len(self.stack1) + len(self.stack2)



#Implement a circular queue that supports wrap-around indexing.
class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = 0
        self.rear = 0
        self.count = 0   # keeps track of number of elements

    def enqueue(self, item):
        if self.count == self.size:
            return "Queue is full!"
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            return "Queue is empty!"
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return item

    def display(self):
        if self.count == 0:
            return "Queue is empty!"
        result = []
        index = self.front
        for _ in range(self.count):
            result.append(self.queue[index])
            index = (index + 1) % self.size
        return result


#Modify the queue so that it can display its current front and rear elements without removing them.

class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, item):
        if self.count == self.size:
            return "Queue is full!"
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            return "Queue is empty!"
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return item

    def display(self):
        if self.count == 0:
            return "Queue is empty!"
        result = []
        index = self.front
        for _ in range(self.count):
            result.append(self.queue[index])
            index = (index + 1) % self.size
        return result

    
    def get_front(self):
        if self.count == 0:
            return "Queue is empty!"
        return self.queue[self.front]

    def get_rear(self):
        if self.count == 0:
            return "Queue is empty!"
        
        return self.queue[(self.rear - 1 + self.size) % self.size]


#Write a function reverseQueue(queue) that reverses all elements of a queue using only standard queue operations.
from collections import deque
def reverseQueue(queue):
    if not queue:
        return"queue is empty"
    stack = []
    while queue:
        stack.append(queue.popleft())
    while stack:
        queue.append(stack.pop())
    return queue

#Implement a queue with max size, where enqueue() raises an error if the queue is full.
class MaxSizeQueue:
    def __init__(self,max_size):

        self.queue=deque()
        self.max.size=max_size

        def enqueue(self,item):
            if len(self.queue)>=self.max_size:
                raise Exception("Queue is full!")
            self.queue.append(item)

        def dequeue(self):
            if not self.queue:
                raise Exception("Queue is empty!")
            return self.queue.popleft()
        
        def is_empty(self):
            return not self.queue
        
        def size(self):
            return len(self.queue)
        
        def display(self):
            return list(self.queue)
        
        
        



        
