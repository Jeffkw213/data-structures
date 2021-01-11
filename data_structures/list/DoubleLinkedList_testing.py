from DoubleLinkedList import Node, doubleLinkedList
list1 = doubleLinkedList()

list1.head = Node("Monday")
n1 = Node("Tuesday")
n2 = Node("Wednesday")

list1.head.next = n1 
n1.pre = list1.head
n1.next = n2
n2.pre = n1

#print (n1.pre.value)
#list1.printList()

list1.add_at_end("Friday")

print(list1.search("Friday"))

list1.push ("Sunday")

list1.insert("Wednesday", "Thursday")
#list1.printList()

list1.delete_node("Wednesday")
list1.printList()