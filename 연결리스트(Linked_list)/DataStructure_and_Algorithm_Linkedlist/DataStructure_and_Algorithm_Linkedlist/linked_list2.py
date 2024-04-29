'''
연결리스트에서의 삽입, 삭제 구현

앞선 파일 linked_list.py 에서는 연결리스트의 삽입시 리스트의 맨 마지막 끝단에만 삽입했었음
그러나, 데이터를 삽입하거나 삭제시 3가지 경우의 수를 생각해 봐야 함.

1. 헤드 부분에 추가, 삭제
2. 중간 부분에 추가, 삭제
3. 꼬리 부분에 추가, 삭제
'''

class Node:
    def __init__(self, data):
        self.data = data    # 노드가 저장되는 데이터
        self.next = None    # 다음 노드를 가리키는 포인터

class LinkedList:
    def __init__(self):
        self.head = None    # 연결 리스트의 첫 번째 노드를 가리키는 포인터
    
    def append(self, data): # 새로운 노드를 리스트의 끝에 추가
        if not self.head:   # 만약 리스트가 비어있으면
            self.head = Node(data)  # 새로운 노드를 head로 지정
        else:
            current = self.head
            while current.next: # 리스트가 비어있지 않을 경우 리스트의 끝을 찾아가는 루프
                current = current.next
            current.next = Node(data)   # 리스트의 끝에 새 노드 추가
    
    def print_list(self):   # 리스트의 모든 노드를 출력해주는 메서드
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def insert(self, data, position):   # 새로운 노드를 리스트의 특정 위치에 삽입
        new_node = Node(data)
        if position == 0:   # 맨 앞에 삽입하는 경우
            new_node.next = self.head   # 새 노드의 다음 노드를 현재의 head로 지정
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                if current:
                    current = current.next
                else:
                    raise IndexError('Position out of range')   # 삽입 위치가 리스트의 길이를 초과하면 예외 발생
            
            if current is None:
                raise IndexError('Position out of range')   # 삽입 위치가 리스트의 길이를 초과하면 예외 발생
            new_node.next = current.next    # 새 노드의 다음 노드를 삽입 위치의 노드로 지정
            current.next = new_node     # 삽입 위치의 앞 노드의 다음 노드를 새 노드로 지정

    def delete(self, data): # delete 메서드는 주어진 값을 가진 노드를 삭제
        if self.head and self.head.data == data:    # 만약 삭제할 노드가 리스트의 앞에 있다면 head를 다음 노드로 이동시킴 
            # 그렇지 않으면 삭제할 노드의 앞 노드의 next를 삭제할 노드의 다음 노드로 변경
            self.head = self.head.next  # head노드를 다음 노드로 지정
        else:
            current = self.head
            while current and current.next and current.next.data != data:   # 삭제할 노드를 찾는 루프
                current = current.next
            if current and current.next:    # 삭제할 노드를 찾은 경우
                current.next = current.next.next    # 삭제할 노드 앞의 노드의 다음 노드를 삭제할 노드의 다음 노드로 지정
            else:
                raise ValueError("Value not found in the list") # 삭제할 노드를 찾지 못한 경우 예외 발생


def __main__():
    linked_list = LinkedList()

    linked_list.append('A')
    linked_list.append('B')
    linked_list.append('C')
    linked_list.append('D')
    linked_list.append('E')

    linked_list.print_list()
    # 출력결과 : A B C D E

    linked_list.insert('F', 0)  # 노드 F를 맨 앞에 삽입
    linked_list.print_list()
    # 출력결과 : F A B C D E

    linked_list.insert('G', 2)  # 노드 G를 index 2 (세 번째 위치)에 삽입
    linked_list.print_list()
    # 출력결과 : F A G B C D E

    linked_list.delete('B')  # 'B' 노드를 삭제
    linked_list.print_list()


    linked_list.delete('E')  # 'E' 노드를 삭제
    linked_list.print_list()

__main__() 