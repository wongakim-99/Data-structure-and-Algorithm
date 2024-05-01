# Double linked list(이중 연결 리스트)
'''
이중 연결 리스트(Double Linked List)는 각 노드가 이전 노드와 다음 노드를 모두 가리키는
연결 리스트다. 각 노드는 이전 노드를 가리키는 'prev'포인터와 다음 노드를 가리키는 'next' 포인터를 가짐
'''

class Node:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = Node(data, prev = self.tail)
            self.tail.next = node
            self.tail = node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next