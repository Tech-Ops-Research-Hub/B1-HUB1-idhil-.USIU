#What makes LifoQueue thread-safe?
#you dont have to manually add locks ,lifoqueue handles  synchronizations for you

#Write a test that demonstrates concurrent stack operations using threading.
from queue import LifoQueue
import threading 
import time

class ThreadSafeStack:
    def __init__(self):
        self.stack = LifoQueue()

    def push(self, item):
        self.stack.put(item)

    def pop(self):
        if not self.stack.empty():
            return self.stack.get()
        return "Stack is empty!"

    def peek(self):
        # No direct peek method, so we handle carefully
        if self.stack.empty():
            return "Stack is empty!"
        temp = []
        while not self.stack.empty():
            temp.append(self.stack.get())
        top_item = temp[-1]
        for item in temp:
            self.stack.put(item)
        return top_item

    def is_empty(self):
        return self.stack.empty()

    def size(self):
        return self.stack.qsize()
    
    def producer(stack):
     for i in range(5):
        stack.push(i)
        print(f"[Producer] Pushed: {i}")
        time.sleep(0.2)  # simulate work


    def consumer(stack):
     while True:
        item = stack.pop()
        if item == "Stack is empty!":
            break
        print(f"[Consumer] Popped: {item}")
        time.sleep(0.3)  # simulate work

    


'''
How can you block a put() operation when the queue is full?
when you create a lifoqueue with a maxsize,the put()method will automatically block if queue is full

Why doesn’t LifoQueue support direct peeking by default?
because of thread safety
'''

