class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class singlelinkedlist:
    def __init__(self):
        self.head = None

    def display_linked_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def insert_at_start(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_position(self, data, index):
        index -= 1
        temp = self.head
        new_node = node(data)
        for i in range(index-1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def delete_at_start(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    def delete_at_end(self):
        temp = self.head.next
        prev = self.head
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None

    def delete_at_position(self, index):
        index -= 1
        prev = self.head
        for i in range(index-1):
            prev = prev.next
        temp = prev.next
        prev.next = temp.next

    def reverse_linked_list(self):
        prev = None
        nxt = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev



sll = singlelinkedlist()
n = node(10)
sll.head = n

n1 = node(20)
n.next = n1

n2 = node(30)
n1.next = n2

n3 = node(40)
n2.next = n3

print("The default Linked list elements:")
sll.display_linked_list()
print()
print("Insert at the beginning of the Linked list:")
sll.insert_at_start(5)
sll.display_linked_list()
print()
print("Insert at the end of the Linked list:")
sll.insert_at_end(50)
sll.display_linked_list()
print()
print("Insert at specific position of the Linked list:")
sll.insert_at_position(25,4)
sll.display_linked_list()
print()
print("Delete at the beginning of the Linked list:")
sll.delete_at_start()
sll.display_linked_list()
print()
print("Delete at the end of the Linked list:")
sll.delete_at_end()
sll.display_linked_list()
print()
print("Delete at specific position of the Linked list:")
sll.delete_at_position(3)
sll.display_linked_list()
print()
print("Reserve of the Linked list:")
sll.reverse_linked_list()
sll.display_linked_list()