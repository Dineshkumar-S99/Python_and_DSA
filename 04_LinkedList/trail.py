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

    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1

    def pop_first_node(self):
        if self.head is None:
            return None
        temp=self.head
        self.head=temp.next
        self.length-=1
        return temp.value
    
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp =self.head
        for _ in range(index):
            temp=temp.next
        return temp
    
    def set_value(self,index,value):
        temp=self.get(index)
        if temp is not None:
            temp.value=value
            return True
        return False

my_ll=LinkedList(10)
my_ll.append(20)
my_ll.append(30)
my_ll.append(40)
my_ll.set_value(7,70)
my_ll.print_ll()