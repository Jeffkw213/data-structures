class Node:
    def __init__ (self, value = None) :
        self.value = value
        self.nextvalue = None


class SLinkedList:
    def __init__ (self):
        self.head = None

#Traversing
    def listprint(self):
        printvalue = self.head
        while printvalue is not None:
            print (printvalue.value)
            printvalue = printvalue.nextvalue
    
    def insert_at_beginning (self, value = None):
        newNode = Node(value)
        
        #Insert new node at the beginning of the list
        newNode.nextvalue = self.head
        self.head = newNode

    def insert_newNode(self, value):
        newNode = Node(value)
        #if the list is empty
        if self.head is None:
            self.head = newNode
            return
        #traverse till the end of the list then insert the value
        last = self.head
        while last.nextvalue is not None:
            last = last.nextvalue
        last.nextvalue = newNode
        
    def search_list (self, value):
        if value is None:
            return 
        
        li = self.head
        while li.nextvalue is not None:
            if li.value is value:
                print("value is in list")
                return
            li = li.nextvalue
        print ("Value not found")
    
    def insert_between(self, pre, value):
        li = self.head
        while li.nextvalue is not None:
            if li.value is pre:
                newNode = Node(value)
                newNode.nextvalue = li.nextvalue
                li.nextvalue = newNode
                return
            li = li.nextvalue
        print("Previous value is not in the list")
    
    def delete_last (self):
        if self.head is None:
            return None
        if self.head.nextvalue is None:
            self.head = None
            return None
        last = self.head
        while last.nextvalue.nextvalue is not None:
            last = last.nextvalue
        last.nextvalue = None
    
    def delete_node (self, value):
        li = self.head
        while li.nextvalue is not None:
            if li.nextvalue.value is value:
                li.nextvalue = li.nextvalue.nextvalue
                return
            li = li.nextvalue
        


list1 = SLinkedList()

list1.head = Node("Monday")
n2 = Node("Tuesday")
n3 = Node("Wednesday")

list1.head.nextvalue = n2

n2.nextvalue = n3

#list1.listprint()

list1.insert_at_beginning("Sunday")

#list1.listprint()

list1.insert_newNode("Friday")
#list1.listprint()

list1.search_list("Friday")
#list1.listprint()

list1.insert_between("Wednesday", "Thursday")
#list1.listprint()

list1.delete_last()
#list1.listprint()

list1.insert_newNode("Saturday")

list1.delete_node("Monday")

list1.listprint()