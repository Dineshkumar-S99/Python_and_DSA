#PREPENDINGing a NODE in LinkedList

#i.e: adding node to the start of the LL

'''
we have two edge cases,for perpendinging the node form the LinkedList 
1. LinkedList could have more than one element in it.
2. Where the LinkedList is already empty'''

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1

    def pop(self):
        if self.length==0:
            return None
        temp=self.head
        pre=self.head
        while temp.next is not None:
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        if self.length==0:
          '''here this one works when after popping the lenght becomes zero and
        for the LinkedList that had only one Node at the very start'''
          self.head=None
          self.tail=None
        return temp.value

    def print_ll(self):
        temp=self.head
        while temp is not None:
            print(temp.value,end=" ")
            temp=temp.next
        print()

    def pop_first_node(self):
        if self.head is None:
          return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length-=1
        if self.length==0:#This will be executed if the length of LL started with 1
          self.tail=None
        return temp.value

my_ll=LinkedList(10)
my_ll.append(20)
my_ll.append(30)
my_ll.print_ll()
print(my_ll.pop())
my_ll.print_ll()
my_ll.prepend(60)
my_ll.print_ll()
print(my_ll.pop())
print(my_ll.pop())
print(my_ll.pop())
my_ll.print_ll()
my_ll.prepend(18)
my_ll.print_ll()