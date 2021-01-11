class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def append(self, value):
        self.items = Node(value, self.items)
        
    def print_stack(self):
        
    