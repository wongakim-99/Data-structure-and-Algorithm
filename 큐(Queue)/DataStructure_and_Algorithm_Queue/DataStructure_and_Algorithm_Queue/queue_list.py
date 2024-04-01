# # Python List를 사용한 Queue

# class ListQueue():
#     def __init__(self):
#         self.queue = []
    
#     def enqueue(self, data):
#         self.queue.append(data)

#     def dequeue(self):
#         dequeue_object = None
#         if self.isEmpty():
#             print("Queue is empty:(")
#         else:
#             dequeue_object = self.queue.pop(0)
#         return dequeue_object

#     def isEmpty(self):
#         is_empty = False
#         if len(self.queue) == 0:
#             is_empty = True 
#         return is_empty
    
# def main():
#     my_queue = ListQueue()

#     # 큐에 데이터 추가
#     print("Pushing elements onto the queue:")
#     my_queue.enqueue(1)
#     my_queue.enqueue(3)
#     my_queue.enqueue(5)
#     my_queue.enqueue(7)
#     my_queue.enqueue(9)

#     # 큐에서 데이터 추출
#     print("\nPopping elements from the queue:")
#     while not my_queue.isEmpty():
#         first_element = my_queue.dequeue()
#         print("dequeued : ", first_element)
#     print("\nqueue is empty :(")

# if __name__ == '__main__':
#     main()


# 파이썬을 활용한 큐

class ListQueue():
    def __init__(self):
        self.queue = []

    def enqueue(self,data):
        self.queue.append(data)
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty :(")
            return None
        else:
            return self.queue.pop(0)
    
    def isEmpty(self):
        return len(self.queue) == 0

def main():
    my_queue = ListQueue()

    # 큐에 데이터 추가
    print("Pushing elements onto the queue")
    my_queue.enqueue(1)
    my_queue.enqueue(3)
    my_queue.enqueue(5)
    my_queue.enqueue(7)
    my_queue.enqueue(9)
    
    # 큐에서 데이터 추출
    print("\nPopping elements from the queue")
    while not my_queue.isEmpty():
        first_element = my_queue.dequeue()
        print("dequeued : ",first_element)
    print("\nqueue is empty:(")

if __name__ == '__main__':
    main()
