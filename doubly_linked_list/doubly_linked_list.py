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
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
            self.length += 1
            return

        if self.head is None:
            self.head = node
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
        self.length += 1
        node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
            return
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
            
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
        if self.head is None:
            self.head = node.value
            return
        if node is self.tail:
            self.remove_from_tail()
            self.add_to_head(node.value)
            return
        self.length -= 1
        node.prev.next = node.next
        node.next.prev = node.prev
        self.add_to_head(node.value)




        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        if node is self.head:
            self.remove_from_head()
            self.add_to_tail(node.value)
            return
        self.length -= 1
        node_next = node.next
        prev_node = node.prev
        node_next.prev = prev_node
        self.add_to_tail(node.value)




    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head is None and self.tail is None:
            return
        if node is self.head and node is self.tail:
            self.tail = None
            self.head = None
            self.length -= 1
            return
        if node is self.head:
            self.remove_from_head()
            return
        if node is self.tail:
            self.remove_from_tail()
            return
        self.length -= 1
        node.prev.next = node.next
        node.next.prev = node.prev




    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head and not self.tail:
            return
        if self.head.next is None:
            return self.head.value
        if self.tail.prev is None:
            return self.tail.value

        start_h = self.head
        max_value = self.head.value
        while start_h is not None:
            if start_h.value > max_value:
                max_value = start_h.value

            start_h = start_h.next
        return max_value







# node_1 = ListNode(5)
# dll = DoublyLinkedList(node_1)
# dll.add_to_head(8)
#
# print(dll.remove_from_head())
