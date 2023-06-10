# Remove Node in a LL

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
    
    def insert_val(self,index,value):
        if index<0 or index>self.length:
            return False
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append(value)
        new_node=Node(value)
        temp=self.get(index-1)
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return True
    
    def remove_node(self,index):
        if index<0 or index>self.length:
            return None
        if index==0:
            return self.pop_first_node()
        if index==self.length:
            return self.pop()
        temp=self.get(index-1)
        var=self.get(index)
        temp.next=var.next
        var.next=None
        self.length-=1
        return var
    
        


my_ll=LinkedList(10)
my_ll.append(20)
my_ll.append(30)
my_ll.append(40)
my_ll.set_value(7,70)
my_ll.print_ll()
my_ll.insert_val(4,6)
my_ll.print_ll()
my_ll.insert_val(0,99)
my_ll.print_ll()
my_ll.insert_val(2,100)
my_ll.print_ll()

my_ll.remove_node(7)
my_ll.print_ll()

my_ll.remove_node(0)
my_ll.print_ll()

my_ll.remove_node(2)
my_ll.print_ll()


#or

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def remove_node_by_index(self, index):
        current = self.head
        previous = None
        position = 0

        # Traverse the linked list to find the node at the desired index
        while current is not None:
            if index == 0:
                # Update the head pointer to the next node
                self.head = current.next
                # Free the memory of the removed node
                current.next = None
                return

            if position == index:
                # Update the links to bypass the current node
                previous.next = current.next
                # Free the memory of the removed node
                current.next = None
                return

            previous = current
            current = current.next
            position += 1

        # Handle case if the index is out of range
        print("Index out of range.")

# Example usage
linked_list = LinkedList()
linked_list.head = Node(1)
second_node = Node(2)
third_node = Node(3)
linked_list.head.next = second_node
second_node.next = third_node
# Removing the node at index 1
linked_list.remove_node_by_index(1)



#or using value
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def remove_node(self, value):
        current = self.head
        previous = None

        # Traverse the linked list to find the node to remove
        while current is not None:
            if current.value == value:
                # Update the links to bypass the current node
                if previous is not None:
                    previous.next = current.next
                else:
                    self.head = current.next
                # Free the memory of the removed node
                current.next = None
                return
            previous = current
            current = current.next

        # Handle case if the node to remove is not found
        print("Node not found in the linked list.")

# Example usage
linked_list = LinkedList()
linked_list.head = Node(1)
second_node = Node(2)
third_node = Node(3)
linked_list.head.next = second_node
second_node.next = third_node

# Removing the node with value 2
linked_list.remove_node(2)