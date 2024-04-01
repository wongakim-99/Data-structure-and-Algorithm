# 파이썬으로 구현한 원형 큐

MAX_QSIZE = 10  # MAX_QSIZE 를 사용하여 원형 큐의 크기를 지정
class CircularQueue:    # 원형 큐 클래스 작성
    def __init__(self): # init 메서드를 사용하여 원형큐에 필요한 front와 rear를 선언
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE # item은 파이썬의 list를 사용하여 None으로 큐의 크기만큼 만들어줌
    
    def isEmpty(self):
        return self.rear == self.front  # 원형큐에서 rear와 front가 같은곳을 가리키고 있으면 큐가 비어있다는 의미
    
    def isFull(self):
        return self.front == (self.front + 1) % MAX_QSIZE   
        # 위의 식에 의하여 front의 값은 MAX_QSIZE - 1 에서 하나 증가되면 0으로 된다.
    
    def clear(self):
        self.front = self.rear  # 큐를 초기화 하기 위해서는 front를 rear가 가리키고 있는 인덱스로 가게해서 원형 큐의 초기상태를 만들어줌
        # self == rear는 큐가 공백상태

    def __len__(self): 
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE # 현재 데이터가 들어있는 큐의 길이
    
    # 원형큐 삽입 알고리즘
    def enqueue(self, data):    
        if not self.isFull():
            self.rear = (self.rear + 1) % MAX_QSIZE # rear값 증가시킨다음
            self.items[self.rear] = data    # rear에다가 데이터 삽입
    
    # 원형큐 삭제 알고리즘
    def dequeue(self):  
        if not self.isEmpty():
            self.front = (self.front + 1) % MAX_QSIZE   # front 값 증가시키고
            return self.items[self.front]   # 데이터 추출

    # 원형 큐가 비어있는지 판단하고 front의 다음 인덱스 안에 있는 값을 반환   
    # 큐 크기와 나머지 연산을 사용해 인덱스 계산
    # 원형큐의 첫번째 삽입된 데이터 보는것 (왜냐하면 큐 특성상 First In First Out)구조이기 때문
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1) % MAX_QSIZE]
        
def main():
    # CircularQueue 객체 생성
    cq = CircularQueue()
    
    # 데이터 삽입
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    
    # 현재 큐의 상태 출력
    print("Current queue:")
    print("Front:", cq.front)
    print("Rear:", cq.rear)
    print("Items:", cq.items)
    print("Length:", len(cq))
    print("Is Queue Full:", cq.isFull())
    print("Is Queue Empty:", cq.isEmpty())
    print("Peek:", cq.peek())
    
    # 데이터 삭제
    deleted_item = cq.dequeue()
    print("\nDeleted item:", deleted_item)
    
    # 현재 큐의 상태 출력
    print("\nCurrent queue after dequeue:")
    print("Front:", cq.front)
    print("Rear:", cq.rear)
    print("Items:", cq.items)
    print("Length:", len(cq))
    print("Is Queue Full:", cq.isFull())
    print("Is Queue Empty:", cq.isEmpty())
    print("Peek:", cq.peek())

if __name__ == "__main__":
    main()
