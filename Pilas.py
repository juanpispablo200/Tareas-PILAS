class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

def decimal_to_binary(decimal):
    stack = Stack()

 
    if decimal == 0:
        return '0'

    while decimal > 0:
        remainder = decimal % 2
        stack.push(str(remainder))
        decimal = decimal // 2

    binary = ''
    while not stack.is_empty():
        binary += stack.pop()

    return binary
decimal = 42
binary = decimal_to_binary(decimal)
print(binary)  

