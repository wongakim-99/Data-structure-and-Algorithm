'''
덱(Deque)이란?

double-ended queue로, 큐의 앞과 뒤 모두에서 삽입 및 삭제가 가능한 큐를 의미한다.
덱은 원형 큐(Circular Queue)를 확장하면 손쉽게 구현 가능
'''


class Deque:
    rear = 0
    front = 0
    MAX_SIZE = 100
    deq = list()

    def __init__(self):
        self.rear = 0
        self.front = 0
        self.deq = [0 for i in range(self.MAX_SIZE)]  # deq라는 리스트에 다 0으로 채움
    
    def is_empty(self): # 덱의 공백상태 검출함수
        if self.rear == self.front:
            return True
        return False
    
    def is_full(self):  # 포화상태 검출함수
        if ((self.rear + 1) % self.MAX_SIZE) == self.front:
            return True
        return False
    
    def get_front(self):    # 현재 덱의 front 값을 반환
        if self.is_empty():
            print("Error : DEQUE IS EMPTY")
            return -1
        self.front = (self.front + 1) % self.MAX_SIZE
        return self.deq[self.front]
    
    def get_rear(self): # 현재 덱의 rear 값을 반환
        if self.is_empty():
            print("ERROR : DEQUE IS EMPTY")
            return -1
        return self.deq[self.rear]
    
    #########################데이터 삽입#########################
    
    def add_rear(self, x):  # 뒤에서 데이터 삽입
        if self.is_full():
            print("ERROR : DEQUE IS FULL")
            return
        self.rear = (self.rear + 1) % (self.MAX_SIZE)
        self.queue = [self.rear] = x

    def add_front(self, x): # 앞에서 데이터 삽입
        if self.is_full():
            print("Error : DEQUE IS FULL")
            return
        self.deq[self.front] = x
        self.front = (self.front - 1 + self.MAX_SIZE) % self.MAX_SIZE

    #########################데이터 삭제#########################
    
    def del_front(self):    # front에서 데이터 삭제
        if self.is_empty():
            print("ERROR : EMPTY")
            return
        self.front = (self.front + 1) % self.MAX_SIZE   # front에서 삭제가 일어날 경우 ,rear값의 변경X -> front + 1 하며 데이터 삭제
        return self.queue[self.front]
    
    def del_rear(self):
        if self.is_empty():
            print("ERROR : EMPTY")
            return
        tmp = self.deq[self.rear]
        self.rear = (self.rear - 1 + self.MAX_SIZE) % self.MAX_SIZE
        return tmp
    
    '''
    rear 에서 삭제가 일어날 경우 front값의 변경 X, rear -= 1을 하며 데이터를 삭제함
    단, 여기서 주의해야 할 점은 self.rear = (self.rear - 1) % MAX_SIZE 연산 X
    왜냐하면 rear변수가 0일 경우 위의 수식을 사용하면 -1이 나와 배열의 인덱스 범위를 벗어남
    따라서 (self.rear - 1 + self.MAX_SIZE) % self.MAX_SIZE 연산을 해줘야함 
    '''

def __main__():
    dq = Deque() # 덱 객체생성

    # 덱에다 데이터 삽입
    for i in range(1, 21):
        dq.add_front(i)

    print("Current Deque")
    print("Current front : ", dq.get_front())
    print("Current rear : ", dq.get_rear())

if __name__ == "__main__":
    __main__()