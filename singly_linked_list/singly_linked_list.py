class Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_head(self):

        if self.head is None:
            return None
        if self.head.next is None:
            head = self.head
            self.head = None
            self.tail = None

            return head.value

        value = self.head.value
        self.head = self.head.next
        return value

    def remove_tail(self):
        if not self.head:
            return None

        if self.head is self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            return value

        current = self.head
        while current.next is not self.tail:
            current = current.next
        value = self.tail.value
        self.tail = current
        return value


    # def print_list(self):
    #     temp = self.head
    #
    #     while(temp):
    #         print(temp.value)
    #         temp = temp.next






#
# ll = LinkedList(Node(5))
#
# second = Node(9)
# third = Node(3)
# ll.head.next = second
# second.next = third
# ll.tail = third
# ll.remove_tail()
# print(ll.tail.value)