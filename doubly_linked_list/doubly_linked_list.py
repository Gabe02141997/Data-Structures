"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next



"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        node = ListNode(value)
        if self.head is None:
            self.head = node
            self.tail = node
            self.length += 1
            return

        head = self.head
        node.next = head
        self.head.prev = node
        self.head = node
        self.length += 1

        return



        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        #what if there is only one node
        #what if there is no head
        if self.head is None:
            return None
        if self.head.next is None:
            head = self.head
            self.length -= 1
            self.head = None
            self.tail = None
            return head.value

        value = self.head.value
        self.head = self.head.next
        self.length -= 1
        return value

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        node = ListNode(value)
        if self.head is None:
            self.head = node
            self.tail = node
            self.length += 1
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.length += 1

        pass
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head is self.tail:
            tail = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
            return tail.value
        self.length -= 1
        tail = self.tail.value
        self.tail.prev.next = None
        self.tail = self.tail.prev
        return tail

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):

        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass




# node_1 = ListNode(5)
# dll = DoublyLinkedList(node_1)
# dll.add_to_head(8)
#
# print(dll.remove_from_head())
