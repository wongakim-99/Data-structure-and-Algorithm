'''
링크드 리스트란?

연결 리스트, 링크드 리스트(linked list)는 각 노드가 데이터와 포인터를
가지고 한 줄로 연결되어 있는 방식으로 데이터를 저장하는 자료 구조이다.
이름에서 말하듯이 데이터를 담고 있는 노드들이 연결되어 있는데, 노드의
포인터가 다음이나 이전의 노드와의 연결을 담당하게 된다.

1. 노드(Node) : 연결 리스트의 기본 단위로서, 데이터를 저장하는 데이터 필드
와 다음 노드를 가리키는 링크 필드로 구성된다.

2. 포인터(pointer) : 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를
가지고 있는 공간

3. 헤드(Head) : 연결 리스트에서 가장 처음 위치하는 노드를 가리킴. 리스트 전체를
참조하는데 사용

4. 테일(Tail) : 연결 리스트에서 가장 마지막 위치하는 노드를 가리킴. 이 노드의
링크 필드는 Null을 가리킨다.
'''

# 노드 클래스 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 연결 리스트 구현
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next: # current.next가 존재하지 않을 때 까지 next를 하기
                current = current.next
            current.next = Node(data)
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

linked_list = LinkedList() # 연결리스트 객체 생성 및 데이터 추가
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

linked_list.print_list()