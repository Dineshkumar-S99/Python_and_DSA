class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True


#### WRITE FIND_KTH_FROM_END FUNCTION HERE ####
#                                             #
#    This is a separate function that is      #
#    not a method within the                  #
#    LinkedList class.                        #
#    Indent all the way to the left.          #
#                                             #
###############################################

def find_kth_from_end(LinkedList,k):
    current_node=LinkedList.head
    include_Kth_node=LinkedList.head
    while (k-1)!=0:
        if include_Kth_node.next is None or include_Kth_node is None:
            return None
        include_Kth_node=include_Kth_node.next
        k-=1
    while include_Kth_node.next is not None:
        include_Kth_node=include_Kth_node.next
        current_node=current_node.next
    return current_node

#or
def find_kth_from_end(LinkedList, k):
    current_node = after_kth_node = LinkedList.head   
    for _ in range(k):
        if after_kth_node is None:
            return None
        after_kth_node = after_kth_node.next
 
    while after_kth_node:
        current_node = current_node.next
        after_kth_node = after_kth_node.next
        
    return current_node
        


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4

k = 3
result = find_kth_from_end(my_linked_list, k)

print(result.value) 

"""
    EXPECTED OUTPUT:
    ----------------
    4
    3
"""