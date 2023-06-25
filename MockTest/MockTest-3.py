class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            raise IndexError("Cannot pop from an empty stack")
    
    def isEmpty(self):
        return len(self.stack) == 0
      
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.isEmpty())

print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack.isEmpty())
