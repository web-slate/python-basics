from testUtils import solution_title, print_and_assert_new, getTestResult
from commonUtils import timeComplexity, spaceComplexity

print('\n >>> Linked List Implementation')
print('>>> 1. Create Node Class with 2 properties 1. data and 2. next property')
print('>>> 2. Create LinkedList Class with property called head')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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

# Example Usage
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

linked_list.print_list()  # Outputs: 1 -> 2 -> 3 -> None
