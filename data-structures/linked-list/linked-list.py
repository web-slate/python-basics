from testUtils import solution_title, print_and_assert_new, getTestResult
from commonUtils import timeComplexity, spaceComplexity

print('\n >>> Linked List Implementation')
print('>>> 1. Create Node Class with 2 properties 1. data and 2. next property')
print('>>> 2. Create LinkedList Class with property called head')
print('''
      Sample Representation of Data
        node(
            data=1,
            next=node(
                data=2,
                next=node(
                    data=3,
                    next=node(
                        data=4,
                        next=None
                    )
                )
            )
        )
''')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListWithoutTail:
    def __init__(self):
        self.head = None

    def append(self, data):
        """ Append a node to the end of the list """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        """ Print all elements of the list """
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next
        print("None")

class LinkedListWithTail:
    def __init__(self):
        self.head = None
        self.tail = None  # Maintaining a reference to the last node

    def append(self, data):
        """ Append a node to the end of the list in O(1) """
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node  # Update the tail reference

    def print_list(self):
        """ Print all elements of the list """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

new_node = Node(1)

solution_title('Linked List without Tail')
linked_list = LinkedListWithoutTail()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

linked_list.print_list()  # Outputs: 1 -> 2 -> 3 -> None

solution_title('Linked List with Tail')
linked_list_2 = LinkedListWithoutTail()
linked_list_2.append(1)
linked_list_2.append(2)
linked_list_2.append(3)

linked_list_2.print_list()  # Outputs: 1 -> 2 -> 3 -> None
