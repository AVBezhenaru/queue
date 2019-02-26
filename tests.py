from queue import *

def roundQueue(n):
    qu = Queue()

    for i in range(n):
        qu.enqueue(i)

    count = n * 2

    while count > 0:
        a = qu.dequeue()
        print(a)
        qu.enqueue(a)
        count -= 1

    return qu

roundQueue(3)


class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.stack == []:
            return None

        return self.stack.pop(0)

    def push(self, value):
        self.stack.insert(0, value)

    def peek(self):
        if self.stack == []:
            return None

        return self.stack[0]


stack = Stack()
stack.push(1)
stack2 = Stack()

count = 1

while count > 0:
    stack2.push(stack.pop())
    stack.push(stack2.pop())
    count -= 1
