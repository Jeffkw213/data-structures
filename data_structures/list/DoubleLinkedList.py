import pylint

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.pre = None


class doubleLinkedList:
    def __init__(self):
        self.head = None
        
    def printList(self):
        printvalue = self.head
        while printvalue is not None:
            print(printvalue.value)
            printvalue = printvalue.next
    
    def search(self, value):
        if self.head is None:
            return None
        li = self.head
        while li is not None:
            if li.value is value:
                return True
            li = li.next
        return False
    
    def add_at_end(self, value):
        newNode = Node(value)
        newNode.next = None
        if self.head is None:
            self.head = newNode
        li = self.head
        while li.next is not None:
            li = li.next
        li.next = newNode
        newNode.pre = li
        
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.head
        newNode.pre = None
        if self.head is None:
            self.head.pre = newNode
        self.head = newNode
    
    def insert_in_empty(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
        else:
            print("not in the list")

    def insert_after_item(self,x, value):
        if self.head is None:
            return
        n = self.head
        while n is not None or n.value is x:
            if n is None:
                print("item is not in the list")
            else:
                newNode = Node(value)
                newNode.pre = n
                newNode.next = n.next
                if n.next is not None:
                    n.next.pre = newNode
                n.next = newNode
            
    
        
    def delete_node(self, x):
        if self.head is None:
            return
        if self.head.next is None:
            if self.head.value is x:
                self.head = None
            else:
                print("Item not found")
            return
        if self.head.value is x:
            self.head = self.head.next
            self.head.pre = None
            return
        
        n = self.head
        while n.next is not None or n.value is x:
            n = n.next 
        
        if n.next is not None:
            n.pre.next = n.next
            n.next.pre = n.pre
        else:
            if n.value is x:
                n.pre.next = None
            else:
                print("element not found")
                
