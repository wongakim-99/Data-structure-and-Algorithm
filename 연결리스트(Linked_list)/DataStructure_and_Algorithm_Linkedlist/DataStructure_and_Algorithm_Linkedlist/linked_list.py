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
# 1. Node 클래스 : 각 노드를 나타내는 클래스. 각 노드는 data와 next라는 두 가지 속성을 지님
class Node:
    def __init__(self, data):
        self.data = data    # data는 노드에 저장된 데이터를 나타냄
        self.next = None    # next는 다음 노드를 가리키는 링크, 초기에 next는 None로 설정됨

# 연결 리스트 구현
class LinkedList:
    def __init__(self):
        self.head = None   # head 속성은 리스트의 첫 번째 노드를 가리킴. 초기에 head는 None로 설정됨

    def append(self, data): 
        # 이 메소드는 연결 리스트의 끝에 새로운 노드를 추가함
        # 만약 리스트가 비어 있다면 head를 새 노드로 설정함.
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next: # 리스트의 끝을 찾아서(current.next가 None이 될 때까지)그곳에 새 노드를 추가함
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

'''
위의 코드에서 LinkedList 클래스는 head를 속성으로 가짐. 이 head는 리스트의 첫 번째 노드를 참조함.
이 head는 리스트의 첫 번째 노드를 참조. append 메소드는 리스트의 끝에 새 노드를 추가하고, print_list메소드는 
리스트의 모든 노드를 출력함
'''