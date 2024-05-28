class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        #new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def is_there_cycle(self):
        slow = self.head
        fast = self.head

        while (slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return True
        return False
    


ll = LinkedList()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
ll.append(n1)
ll.append(n2)
ll.append(n3)
print(ll.is_there_cycle())
ll.append(n1)
print(ll.is_there_cycle())